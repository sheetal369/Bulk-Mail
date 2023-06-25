from django.shortcuts import HttpResponse, render,get_object_or_404
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from emailsender.forms import *
from django.urls import reverse
from django.shortcuts import redirect
from emailsender.models import *
from html2text import HTML2Text
@login_required
def index(request):
    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['mailBox']
        converter = HTML2Text()
        converter.ignore_links = True  # Ignore hyperlinks
        plain_text = converter.handle(message)
        selected_id = request.POST.getlist('group')
        selected_groups=[Group.objects.get(id=i) for i in selected_id]
        message_id = request.POST.get('message_id')
        if message_id:
            saved_message = Message.objects.get(id=message_id)
            saved_message.subject=subject
            saved_message.message=plain_text
            for g in selected_groups:
                saved_message.message_group.add(g)
            if 'sent' in request.POST:
                emails=((selected_group.emails.values_list('email_address', flat=True)) for selected_group in selected_groups)
                all_emails=[email for sublist in emails for email in sublist]
                email_message = EmailMultiAlternatives(subject, message, to=all_emails)#Send Email to all emails 
                email_message.content_subtype='html'
                email_message.send()
                saved_message.status=Message.Status.SENT
                saved_message.save()
                return redirect(reverse('sent_success', args=(saved_message.id,)))
            elif 'draft' in request.POST:
                saved_message.status=Message.Status.DRAFT
                saved_message.save()
                return redirect(reverse('save_to_draft'))  
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

@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_contacts') 
    else:
        form = UserForm()
    return render(request, 'create_contact.html', {'form': form})

@login_required
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
       
@login_required
def delete_user(request):
    if request.POST:
        id = request.POST.get('id')
        user = User.objects.get(id = id)
        user.delete()
        return redirect(reverse("view_contacts"))
    else:
        HttpResponse("Operation Denied")
@login_required
def view_contacts(request):
    contacts = User.objects.all()
    return render(request, 'contacts.html', {"contacts":contacts})

@login_required
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
@login_required
def view_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {"groups":groups})
@login_required
def group_detail(request, id):
    group = get_object_or_404(Group, id = id)
    contacts = group.emails.all()
    context = {
        'group': group,
        'contacts': contacts
    }
    return render(request, 'group.html', context)


@login_required
def sent_success(request,id):
    message=get_object_or_404(Message, id=id)
    sent_groups=message.message_group.all()
    return render(request,'sentsuccess.html',{'sent_groups':sent_groups})

@login_required
def save_to_draft(request):
    return render(request,'save_to_draft.html')

@login_required
def all_mails(request):
    sent_mails=Message.objects.filter(status=Message.Status.SENT)
    draft_mails=Message.objects.filter(status=Message.Status.DRAFT)
    context ={'sent_mails':sent_mails, 'draft_mails': draft_mails}
    return render(request,'all_mails.html',context)

@login_required    
def edit_mails(request,id):
    message=get_object_or_404(Message,id=id)
    groups=Group.objects.all()
    return render(request,'index.html',{'groups':groups,
                                        'message':message})
@login_required
def delete_mails(request,):
    if request.method=='POST':
        id=request.POST.get('id')
        message=Message.objects.get(id=id)
        message.delete()
        return redirect(reverse('all_mails'))

    
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('all_mails'))
               
    else:
        form = LoginForm()

    return render(request, 'login.html', {'login': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('login_user'))