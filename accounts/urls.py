from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url 
from django.views.static import serve



app_name = 'accounts'

urlpatterns = [
    path('signup/', sign_up, name='sign_up'),
    path('register', sign_up, name='sign_up'),
    path('sign_in', sign_in, name='sign_in'),
    path('login/', sign_in, name='sign_in'),
    path('logout', user_logout, name='logout'),
    path('profile', profile, name='profile'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)