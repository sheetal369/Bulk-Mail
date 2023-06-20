from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse

class Group(models.Model):
    name = models.CharField(max_length=60, unique=True)
    emails=models.ManyToManyField('User',related_name='groups')
    description=models.TextField()

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
    
class Sent(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Message.Status.SENT)
class Draft(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Message.Status.DRAFT)

class Message(models.Model):
    class Status(models.TextChoices):
        DRAFT ='DF', 'Draft'
        SENT ='ST', 'Sent'
    group = models.ManyToManyField(Group, name='message_group',related_name="groups")
    subject = models.CharField(max_length=255)
    content = models.TextField()
    status= models.CharField(max_length=2,
                             choices=Status.choices,
                             default=Status.DRAFT)
    sent=Sent()
    draft=Draft()
    created_at = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
    def __str__(self) -> str:
        return self.subject

