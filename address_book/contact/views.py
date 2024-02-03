from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from contact.models import Contact, Event
from contact.serializers import ContactSerializer, EventSerializer


class ContactList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRetrieve(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactUpdate(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDestroy(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreate(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CreateContact(APIView):
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(APIView):
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()

        date_time = self.request.query_params.get('date_time', None)
        if date_time is not None:
            queryset = queryset.filter(date_time=date_time)

        return queryset
