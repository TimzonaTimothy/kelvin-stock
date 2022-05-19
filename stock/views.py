from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib import messages
from accounts.models import Account


def home(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def contact(request):
    if request.method == "POST":
        message_full_name = request.POST['full_name']  
        message_email = request.POST['email']
        message_subject = request.POST['message_subject']
        message = request.POST['message']

        send_mail(
           message_full_name +' sent you an enquiry '+ message_email + ' \n'+ message_subject,
            message,
            'arizonatymothy@gmail.com',
            ['arizonatymothy@gmail.com',],
            fail_silently=False
        )
        messages.success(request, 'Dear ' + message_full_name+' Your email has been sent ','alert alert-success alert-dismissible')
        return render(request, 'contact.html', {})
    return render(request, "contact.html", {})


def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)


            current_site = get_current_site(request)
            mail_subject = 'Reset your password'
            message = render_to_string('account/reset_password_email.html', {
                'user' : user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('/accounts/sign_in')


        else:
            messages.error(request, 'Account does not exists!')
            return redirect('forgetpassword')
    return render(request, "account/forgetpassword.html", {})


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('/resetpassword')
    
    else:
        messages.error(request, 'This link has expired!')
        return redirect('/accounts/sign_in')

def resetpassword(request):
    if request.method == 'POST':
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if password == confirm_password:
                uid = request.session.get('uid')
                user = Account.objects.get(pk=uid)
                user.set_password(password)
                user.save()
                messages.success(request, 'Password reset successful')
                return redirect('/accounts/sign_in')

            else:
                messages.error(request, 'Password do not match')
                return redirect('/resetpassword')
    else:
        return render(request, 'account/resetpassword.html')