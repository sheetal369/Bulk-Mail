from django.shortcuts import HttpResponse, render,get_object_or_404
from django.core.mail import EmailMessage,EmailMultiAlternatives
from emailsender.forms import *
from django.urls import reverse
from django.shortcuts import redirect
from emailsender.models import *
from html2text import HTML2Text

def index(request):
    if request.method=='POST':
        if 'sent' in request.POST:
            subject=request.POST['subject']
            message=request.POST['mailBox']
            converter = HTML2Text()
            converter.ignore_links = True  # Ignore hyperlinks
            plain_text = converter.handle(message)
            selected_id = request.POST.getlist('group')
            selected_groups=[Group.objects.get(id=i) for i in selected_id]
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
            subject=request.POST['subject']
            message=request.POST['mailBox']
            converter = HTML2Text()
            converter.ignore_links = True  # Ignore hyperlinks
            plain_text = converter.handle(message)
            selected_id = request.POST.getlist('group')
            selected_groups=[Group.objects.get(id=i) for i in selected_id]
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

def edit_user(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.full_name = request.POST['full_name']
        user.phone_number = request.POST['phone_number']
        user.email_address = request.POST['email_address']
        user.save()
        return redirect('view_contacts')

    user = User.objects.get(id=id)
    return render(request, 'edit_contact.html', {'contact': user})        

def delete_user(request):
    if request.POST:
        id = request.POST.get('id')
        user = get_object_or_404(User, id)
        user.delete()
        return redirect(reverse("view_contacts"))

def view_contacts(request):
    contacts = User.objects.all()
    return render(request, 'contacts.html', {"contacts":contacts})


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

def view_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {"groups":groups})

def group_detail(request, id):
    group = get_object_or_404(Group, id = id)
    contacts = group.emails.all()
    context = {
        'group': group,
        'contacts': contacts
    }
    print(contacts)
    return render(request, 'group.html', context)


def sent_success(request,id):
    message=get_object_or_404(Message, id=id)
    sent_groups=message.message_group.all()
    return render(request,'sentsuccess.html',{'sent_groups':sent_groups})

def save_to_draft(request):
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

def delete_mail(request):
    if request.POST:
        id = request.POST.get('id')
        message = get_object_or_404(Message, id = id)
        message.delete()
        return redirect(reverse("all_mails"))

def login(request):
    return render(request, 'login.html')