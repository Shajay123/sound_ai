from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_issue')  
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_list(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 5)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'contact_list.html', {'page_obj': page_obj})

@csrf_exempt
def update_status(request, contact_id):
    if request.method == 'POST':
        contact = get_object_or_404(Contact, pk=contact_id)
        contact.status = 'Sent'
        contact.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)



def payment_issue(request):
    return render(request, 'success.html')