from django.contrib import admin
from .models import Group, Email

# Register your models here.
@admin.register(Group)
class GroupRegister(admin.ModelAdmin):
    list_display=['id','name','Associated_Emails']
    def Associated_Emails(self, obj):
        return ",".join([email.email_address for email in obj.emails.all()])
   
@admin.register(Email)
class EmailRegister(admin.ModelAdmin):
    list_display=['id','email_address','group']
    def group(self, obj):
        return ",".join([groups.name for groups in obj.groups.all()])
