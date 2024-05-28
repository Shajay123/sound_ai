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