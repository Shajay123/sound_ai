# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('update_status/<int:contact_id>/', views.update_status, name='update_status'),
    path('payment-issue/', views.payment_issue, name='payment_issue'),
]
