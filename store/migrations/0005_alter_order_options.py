# Generated by Django 4.1.2 on 2022-10-25 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_customer_email_remove_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can Cancel order')]},
        ),
    ]