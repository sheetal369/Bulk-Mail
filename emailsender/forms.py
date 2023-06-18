from django import forms
from .models import Group,Email


class CreateGroup(forms.Form):
    name=forms.CharField(required=True,max_length=50)
    emails=forms.ModelMultipleChoiceField(queryset=Email.objects.all())

class GroupEmailForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

    def clean_group(self):
        group = self.cleaned_data['group']
        if not group.emails.exists():
            raise forms.ValidationError("The selected group doesn't have any email addresses.")
        return group