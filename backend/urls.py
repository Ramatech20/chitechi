"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home, about_us, contacts, events, gallery, leadership, membership, news
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('leadership/', leadership, name='leadership'),
    path('membership/', membership, name='membership'),
    path('news/', news, name='news'),
    path('admin/', admin.site.urls),
    path('api/', include('donations.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
