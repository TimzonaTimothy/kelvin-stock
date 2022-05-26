from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url 
from django.views.static import serve




urlpatterns = [
    path('deposit', deposit, name="deposit"),
    path('deposited/', deposit_complete, name='deposit_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)