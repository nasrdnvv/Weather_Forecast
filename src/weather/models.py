from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    favorite_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username