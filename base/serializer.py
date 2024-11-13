# connect between the views.py to the database

from rest_framework import serializers
from .models import Babysitter, Meetings, Requests, TimeWindow
from .models import Parents
from .models import Kids
from .models import Reviews
from .models import Availability
from django.contrib.auth.models import User



class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value
            



class BabysitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Babysitter
        fields = '__all__'



class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'


class KidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kids
        fields = '__all__'


class MeetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'


class TimeWindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeWindow
        fields = '__all__'


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'


