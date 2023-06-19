from django.shortcuts import HttpResponse, render
from emailsender.forms import *
from django.urls import reverse
from django.shortcuts import redirect
from emailsender.models import *

def index(request):
    return render(request,'index.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_contacts')  # Redirect to the user list view after successful creation
    else:
        form = UserForm()
    return render(request, 'create_contact.html', {'form': form})


def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        description = request.POST.get('mailBox')
        contacts = request.POST.getlist('check_status')
        
        users = [User.objects.get(id = i) for i in contacts]
        group = Group.objects.create(name=group_name, description=description)
        group.emails.add(*users)
        
        return redirect(reverse(view_groups))

    contacts = User.objects.all()
    return render(request, 'create_group.html', {"contacts":contacts})

def view_contacts(request):
    contacts = User.objects.all()
    return render(request, 'contacts.html', {"contacts":contacts})

# def create_group(request):
#     contacts = User.objects.all()
#     return render(request, 'create_group.html', {"contacts":contacts})

def view_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {"groups":groups})

def group_detail(request):
    return render(request, 'group.html')