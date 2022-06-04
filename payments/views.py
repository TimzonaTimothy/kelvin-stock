from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from accounts.models import Account
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import JsonResponse
from .models import *
import json
# Create your views here.

@login_required(login_url='login')
def deposit(request):
    
    if request.is_ajax():
        amount = request.POST.get('amount', False)
        ref =  request.POST.get('ref', False)
        user = request.user
        if request.user.is_authenticated:
            deposit = Payment.objects.create(amount_paid=amount,ref=ref,user=user,)
            deposit.verified = True
            deposit.save();
            deposited = True
            messages.success(request, 'Success, Deposit Successful')   
            if deposited == True:
                
                messages.success(request, 'Deposit, Successful')

                 
                 
                return JsonResponse({'deposited':deposited})

       
                
@login_required(login_url='login')
def deposit_complete(request):
    ref = request.GET.get('ref')
    try:
        paid = Payment.objects.get(ref=ref,user=request.user) 
        context={
            'paid':paid
        }
        return render(request, 'includes/deposit_complete.html', context)
    except(Payment.DoesNotExist):
        return redirect('/')