from django.contrib import admin
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number','status','language', 'content')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('email',)
    ordering = ('-id',)
