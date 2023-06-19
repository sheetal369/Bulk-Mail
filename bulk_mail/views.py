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
        name = request.POST['name']
        description = request.POST['mailBox']
        contacts = request.POST.getlist('check_status')  # Assuming 'contacts' is the name attribute of the checkbox inputs
        print(contacts)
        return HttpResponse(contacts)
        # Create the group
        group = Group.objects.create(name=name, description=description)

        # Add contacts to the group
        for contact_id in contacts:
            group.emails.add(contact_id)

        # Redirect to the group detail page or any other appropriate URL
        return redirect('group_detail', id=group.id)

    # If the request method is not POST, render the form template
    return render(request, 'compose_mail.html')

def view_contacts(request):
    contacts = User.objects.all()
    return render(request, 'contacts.html', {"contacts":contacts})

def create_group(request):
    contacts = User.objects.all()
    return render(request, 'create_group.html', {"contacts":contacts})

def view_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {"groups":groups})

def group_detail(request):
    return render(request, 'group.html')