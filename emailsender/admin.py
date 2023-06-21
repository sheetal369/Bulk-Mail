from django.contrib import admin
from .models import Group, User, Message

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'associated_users']
    
    def associated_users(self, obj):
        return ", ".join([email.email_address for email in obj.emails.all()])
    associated_users.short_description = 'Associated Users'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email_address', 'phone_number']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'associated_groups', 'subject', 'created_at','status']
    def associated_groups(self, obj):
        return ", ".join([g.name for g in obj.message_group.all()])
