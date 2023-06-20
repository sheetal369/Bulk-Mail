from django.db import models
from django.urls import reverse

class Group(models.Model):
    name=models.CharField(max_length=60,unique=True)
    description=models.TextField()
    emails=models.ManyToManyField('Email',related_name='groups')

    def __str__(self):
        return self.name
    
    @property
    def members_count(self):
        return self.emails.count()
    
    def get_absolute_url(self):
        return reverse("group", kwargs={"id": self.id})

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True, null=False, max_length=40)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.email_address

class Message(models.Model):
    group = models.ManyToManyField(Group, name='message_group')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
