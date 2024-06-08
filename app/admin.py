from django.contrib import admin
from django.contrib import admin
from .models import Contact, Payment

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number','status','language', 'content')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('email',)
    ordering = ('-id',)

    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('contact', 'razorpay_order_id', 'razorpay_payment_id', 'status', 'created_at')
    search_fields = ('razorpay_order_id', 'razorpay_payment_id', 'status')
    list_filter = ('status', 'created_at')
    date_hierarchy = 'created_at'