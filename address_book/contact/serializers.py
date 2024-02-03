from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Contact, Event


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id', 'first_name', 'last_name', 'country', 'city', 'street', 'url', 'phone'
        ]


class EventSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time', 'location', 'contacts']

