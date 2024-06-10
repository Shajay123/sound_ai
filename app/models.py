from django.db import models

class Contact(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Sent', 'Sent'),
    ]

    INDIAN_LANGUAGES = [
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Tamil', 'Tamil'),
        ('Telugu', 'Telugu'),
        ('Kannada', 'Kannada'),
        ('Malayalam', 'Malayalam'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    language = models.CharField(max_length=50, choices=INDIAN_LANGUAGES)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['phone_number']),
            models.Index(fields=['status']),
        ]
        ordering = ['-created_at']
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

class Payment(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=100, unique=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.razorpay_order_id
    
    class Meta:
        indexes = [
            models.Index(fields=['razorpay_order_id']),
            models.Index(fields=['status']),
        ]
        ordering = ['-created_at']
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
