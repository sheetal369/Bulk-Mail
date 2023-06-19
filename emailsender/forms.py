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
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

    def clean_group(self):
        group = self.cleaned_data['group']
        if not group.emails.exists():
            raise forms.ValidationError("The selected group doesn't have any email addresses.")
        return group