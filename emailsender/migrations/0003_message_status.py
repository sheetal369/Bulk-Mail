# Generated by Django 4.2.2 on 2023-06-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailsender', '0002_remove_message_message_group_message_message_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('DF', 'DRAFT'), ('ST', 'SENT')], default='DF', max_length=2),
        ),
    ]
