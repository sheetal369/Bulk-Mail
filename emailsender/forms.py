from django import forms
from .models import Group, User


class CreateGroup(forms.Form):
    name=forms.CharField(required=True,max_length=50)
    emails=forms.ModelMultipleChoiceField(queryset=User.objects.values_list('email_address', flat=True))

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email_address', 'phone_number']


class GroupEmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.Textarea()
    group= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    