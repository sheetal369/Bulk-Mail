from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=60, unique=True)
    emails=models.ManyToManyField('User',related_name='groups')
    description=models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True, null=False, max_length=40)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.email_address

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
