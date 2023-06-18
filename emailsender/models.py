from django.db import models

# Create your models here.

class Group(models.Model):
    name=models.CharField(max_length=60,unique=True)
    description=models.TextField()
    emails=models.ManyToManyField('Email',related_name='groups')
    def __str__(self):
        return self.name
    
class Email(models.Model):
    email_address= models.EmailField(unique=True,null=False,max_length=40)
    def __str__(self):
        return self.email_address
    
class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
