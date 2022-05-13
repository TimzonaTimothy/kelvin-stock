from django.shortcuts import get_object_or_404, render, redirect
from accounts.models import *
from .models import *
from django.db.models import Q
from django.http import HttpResponse
import os
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
# import magic
# Create your views here.
def store(request, category_slug=None):
    categories = None 
    stocks = None


    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        stocks = Stock.objects.filter(category=categories, )
        paginator = Paginator(stocks, 2)
        page = request.GET.get('page')
        paged_stocks = paginator.get_page(page)
        stock_count = stocks.count()

    else:

        stocks = Stock.objects.all().order_by('-id')
        paginator = Paginator(stocks, 2)
        page = request.GET.get('page')
        paged_stocks = paginator.get_page(page)
        stock_count = stocks.count()

    context = {
        'stocks':paged_stocks,
        'stock_count':stock_count
    }
    return render(request, 'store.html', context)



@login_required(login_url = '')
def stock_detail(request, id):
    stock = Stock.objects.get(id=id)
    # if stock.images.exits():
    #     stock = Stock.objects.get(id=id)
    #     image_buffer = open(stock.file.path, "rb").read()
    #     content_type = magic.from_buffer(image_buffer, mime=True)
    #     response = HttpResponse(image_buffer, content_type=content_type);
    #     response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(stock.file.path)
    #     return response
    return render(request, 'product-view.html', {'stock':stock})


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            stocks = Stock.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(stock_name__icontains=keyword))
            stock_count = stocks.count()
    context = {
        'stocks':stocks,
        'stock_count':stock_count
        }
    
    return render(request, 'store.html', context)

