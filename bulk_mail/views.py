from django.shortcuts import HttpResponse, render

def index(request):
    return render(request,'index.html')

def create_contact(request):
    return render(request, 'create_contact.html')

def view_contacts(request):
    return render(request, 'contacts.html')

def create_group(request):
    return render(request, 'create_group.html')

def view_groups(request):
    return render(request, 'groups.html')

def view_group(request):
    return render(request, 'group.html')