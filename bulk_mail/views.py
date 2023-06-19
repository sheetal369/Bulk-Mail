from django.shortcuts import HttpResponse, render
from emailsender.forms import *
from django.urls import reverse
from django.shortcuts import redirect
from emailsender.models import *

def index(request):
    return render(request,'base.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_contacts')  # Redirect to the user list view after successful creation
    else:
        form = UserForm()
    return render(request, 'create_contact.html', {'form': form})


def view_contacts(request):
    contacts = User.objects.all()
    return render(request, 'contacts.html', {"contacts":contacts})

def create_group(request):
    return render(request, 'create_group.html')

def view_groups(request):
    return render(request, 'groups.html')

def view_group(request):
    return render(request, 'group.html')