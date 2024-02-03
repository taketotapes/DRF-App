from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    url = models.URLField(max_length=200, unique=True)
    phone = models.CharField(max_length=30)

    class Meta:
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=128)
    contacts = models.ManyToManyField(Contact, related_name='events')

    class Meta:
        unique_together = ['title', 'description', 'date_time', 'location']

    def __str__(self):
        return f'Events info: {self.title}-{self.description}-{self.date_time}-{self.location}'
