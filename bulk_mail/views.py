from django.shortcuts import HttpResponse, render,get_object_or_404
from django.core.mail import EmailMessage,EmailMultiAlternatives
from emailsender.forms import *
from django.urls import reverse
from django.shortcuts import redirect
from emailsender.models import *
import html2text

def index(request):
    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['mailBox']
        converter = html2text.HTML2Text()
        converter.ignore_links = True  # Ignore hyperlinks
        plain_text = converter.handle(message)
        selected_id = request.POST.getlist('group')
        selected_groups=[Group.objects.get(id=i) for i in (selected_id)]
        if 'sent' in request.POST:
            emails=((selected_group.emails.values_list('email_address', flat=True)) for selected_group in selected_groups)
            all_emails=[email for sublist in emails for email in sublist]
            email_message = EmailMultiAlternatives(subject, message, to=all_emails)#Send Email to all emails 
            email_message.content_subtype='html'
            email_message.send()
            message=Message.objects.create(
                    subject=subject,
                    content=plain_text,
                    status=Message.Status.SENT
                )
            for g in selected_groups:
                message.message_group.add(g)
            return redirect(reverse('sent_success', args=(message.id,)))
        if 'draft' in request.POST:
            message=Message.objects.create(
                    subject=subject,
                    content=plain_text,
                    status=Message.Status.DRAFT
                )
            for g in selected_groups:
                message.message_group.add(g)
            return redirect(reverse('save_to_draft'))
    groups=Group.objects.all()
    return render(request,'index.html',{'groups':groups})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_contacts') 
    else:
        form = UserForm()
    return render(request, 'create_contact.html', {'form': form})

def delete_user(request, id):
    if request.GET:
        id = request.GET.get('id')
        user = User.objects.get(id = id)
        user.delete()
        return redirect(reverse("view_contacts"))
    else:
        HttpResponse("Operation Denied")



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

def view_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {"groups":groups})

def group_detail(request):
    return render(request, 'group.html')

def sent_success(request,id):
    message=get_object_or_404(Message, id=id)
    sent_groups=message.message_group.all()
    return render(request,'sentsuccess.html',{'sent_groups':sent_groups})
def save_to_draft(request,):
    return render(request,'save_to_draft.html')
def all_mails(request):
    sent_mails=Message.objects.filter(status=Message.Status.SENT)
    draft_mails=Message.objects.filter(status=Message.Status.SENT)
    context ={'sent_mails':sent_mails, 'draft_mails': draft_mails}
    return render(request,'all_mails.html',context)
    
def edit_mails(request,id):
    message=get_object_or_404(Message,id=id)
    groups=Group.objects.all()
    return render(request,'index.html',{'groups':groups,
                                        'message':message})
    
