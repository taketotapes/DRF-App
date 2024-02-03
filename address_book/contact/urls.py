from contact.views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, EventViewSet


router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', ContactList.as_view(), name='contact_list'),
    path('create/', ContactCreate.as_view(), name='contact_create'),
    path('<int:pk>/', ContactRetrieve.as_view(), name='contact_retrieve'),
    path('<int:pk>/delete/', ContactDestroy.as_view(), name='contact_delete'),
    path('<int:pk>/update/', ContactUpdate.as_view(), name='contact_update'),
    path('', include(router.urls)),
]
