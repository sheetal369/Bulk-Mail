from django.shortcuts import HttpResponse, render

def index(request):
    return render(request,'base/base.html')

def create_contacts(request):
    return render(request, 'createcontact.html')