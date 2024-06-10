# Generated by Django 3.2.8 on 2024-06-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_payment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_at'], 'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-created_at'], 'verbose_name': 'Payment', 'verbose_name_plural': 'Payments'},
        ),
        migrations.AlterField(
            model_name='payment',
            name='razorpay_order_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['email'], name='app_contact_email_60d827_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['phone_number'], name='app_contact_phone_n_dd57aa_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['status'], name='app_contact_status_a2047c_idx'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['razorpay_order_id'], name='app_payment_razorpa_9aeb6f_idx'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['status'], name='app_payment_status_2b66c3_idx'),
        ),
    ]
