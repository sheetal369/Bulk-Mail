from django.shortcuts import HttpResponse, render,get_object_or_404
from django.core.mail import EmailMessage,EmailMultiAlternatives
from emailsender.forms import *
from django.urls import reverse
from django.shortcuts import redirect
from emailsender.models import *

def index(request):
    groups=Group.objects.all()
    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['mailBox']
        selected_id = request.POST.getlist('group')
        selected_groups=[Group.objects.get(id=i) for i in selected_id]
        emails=((selected_group.emails.values_list('email_address', flat=True)) for selected_group in selected_groups)
        all_emails=[email for sublist in emails for email in sublist]
        email_message = EmailMultiAlternatives(subject, message, to=all_emails)#Send Email to all emails 
        email_message.content_subtype='html'
        email_message.send()
        message=Message.objects.create(
                subject=subject,
                content=message,
            )
        for g in selected_groups:
            message.message_group.add(g)
        
        
        return redirect(reverse('sent_success', args=(message.id,)))

        
    return render(request,'index.html',{'groups':groups})

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

def sent_success(request,id):
    message=get_object_or_404(Message, id=id)
    sent_groups=message.message_group.all()
    return render(request,'sentsuccess.html',{'sent_groups':sent_groups})