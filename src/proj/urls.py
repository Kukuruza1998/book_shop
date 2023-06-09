"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from homepage import views as  homepage_views
from django.conf import settings 
from django.conf.urls.static import static
from comments import urls as comments_urls

urlpatterns = [
    path('s-admin/', admin.site.urls),
    path('directories/', include('directories.urls', namespace='directories')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('search/', include('search.urls', namespace='search')),
    path('comments/', include(comments_urls, namespace='comments')),
    path('profile/', include('user_profile.urls', namespace='user_profile')),
    path('', homepage_views.HomePage.as_view(), name= 'homepage'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
