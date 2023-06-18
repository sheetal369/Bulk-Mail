from django.shortcuts import render
from .forms import GroupEmailForm,CreateGroup
from .models import Group, Email, Message
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def create_group(request):
    if request.method=='POST':
        form = CreateGroup(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            emails=form.cleaned_data['emails']
            group=Group.objects.create(name=name)
            group.emails.add(*emails)
            return HttpResponse("Group Created")
    else:
        form=CreateGroup()
    return render(request,'emailsender/create_group.html',{'form':form})


