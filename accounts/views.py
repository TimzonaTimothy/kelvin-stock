from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import update_session_auth_hash
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
import requests
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.





def sign_in(request):


    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = auth.authenticate(email=email, password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, ', Welcome '+user.first_name)

                url = request.META.get('HTTP_REFFERER')
                try:
                    query = requests.utils.urlparse(url).query
                    params = dict(x.split('=') for x in query.split('&'))
                    if 'next' in params:
                        nextpage = params['next']
                        return redirect(nextpage)
                except:
                    return redirect('/accounts/profile') 
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('/accounts/sign_in')
        else:
            return render(request, 'account/login.html',{})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('/accounts/sign_in')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('/accounts/sign_up')



def sign_up(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method == 'POST':
            
            first_name = request.POST['first_name']
            # last_name = form.cleaned_data['last_name']
            email = request.POST['email']
            password = request.POST['password']
            username = email.split('@')[0]
            last_name = ''
                
            if Account.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exists')
                return redirect('/accounts/sign_up')
            if Account.objects.filter(email=email, is_active=False).exists():
                messages.warning(request, 'Email already exists')
                return redirect('/accounts/sign_up')
                    
                    
            user = Account.objects.create_user(first_name=first_name,last_name= last_name, email=email, username=username,password=password,)
            
                
        
                
                #user_activation
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('account/account_verification_email.html', {
                'user' : user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Thank you for registrating with us. We have sent you a verification email to your email address. Please verify it.')
            return redirect('/accounts/sign_in')
            
        else:
            return render(request, 'account/register.html', {})




def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required(login_url = '')
def profile(request):
    account = Account.objects.get(email=request.user.email)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_pix = request.FILES.get('profile_picture')
            

        account.first_name = first_name
        account.last_name = last_name
        account.email = email
        account.profile_picture = profile_pix
        account.save()
        messages.success(request, "Profile Updated")
        return redirect('/accounts/profile') 
    return render(request, 'account/profile.html', {})