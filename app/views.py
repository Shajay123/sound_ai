from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Contact, Payment
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import ContactForm
import razorpay
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('create_payment', contact_id=contact.id)
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

@csrf_exempt
def create_payment(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    amount_in_rupees = 250  # Amount in INR
    amount_in_paisa = amount_in_rupees * 100  # Convert to paisa

    payment = client.order.create({
        'amount': amount_in_paisa,
        'currency': 'INR',
        'payment_capture': 1
    })

    Payment.objects.create(
        contact=contact,
        razorpay_order_id=payment['id']
    )

    return render(request, 'payment.html', {
        'payment': payment,
        'contact': contact,
        'key_id': settings.RAZORPAY_KEY_ID,
        'amount_in_rupees': amount_in_rupees
    })

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        data = request.POST
        try:
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            client.utility.verify_payment_signature(data)
            payment = Payment.objects.get(razorpay_order_id=data['razorpay_order_id'])
            payment.razorpay_payment_id = data['razorpay_payment_id']
            payment.razorpay_signature = data['razorpay_signature']
            payment.status = 'Success'
            payment.save()
        except razorpay.errors.SignatureVerificationError:
            logger.error('Payment verification failed for order ID: %s', data.get('razorpay_order_id'))
            return JsonResponse({'error': 'Payment verification failed'}, status=400)
    return redirect('home')

def contact_list(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    for contact in page_obj:
        contact.payment = Payment.objects.filter(contact=contact).first()

    return render(request, 'contact_list.html', {'page_obj': page_obj})

@csrf_protect
def update_status(request, contact_id):
    if request.method == 'POST':
        contact = get_object_or_404(Contact, pk=contact_id)
        contact.status = 'Sent'
        contact.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

def payment_issue(request):
    return render(request, 'payment_issue.html')  # Ensure the template name matches the context
