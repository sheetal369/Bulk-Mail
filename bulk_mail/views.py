from django.shortcuts import HttpResponse, render

def index(request):
    return render(request,'index.html')

def create_contacts(request):
    return render(request, 'createcontact.html')