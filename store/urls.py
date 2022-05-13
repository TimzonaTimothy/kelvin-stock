from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url 
from django.views.static import serve



app_name = 'store'

urlpatterns = [
    path('', store, name='store'),
    path('search/', search, name='search'),
    path('<slug:category_slug>/', store, name='stock_by_category'),
    path('stock_detail/<int:id>/', stock_detail, name='stock_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)