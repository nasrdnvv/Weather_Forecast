from rest_framework.serializers import ModelSerializer
from .models import Location, User

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'