"""
URL configuration for address_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.urls import include
from django.conf.urls.static import static
from contact.views import CreateContact, ContactDetail, ContactList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('list/', ContactList.as_view(), name='contact-list'),
    path('contact/create/', CreateContact.as_view(), name='create_contact'),
    path('detail/<int:pk>/', ContactDetail.as_view(), name='contact_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

