# Generated by Django 4.2.2 on 2023-06-20 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsender', '0003_message_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='status',
        ),
    ]
