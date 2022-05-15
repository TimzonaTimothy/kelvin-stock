from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


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