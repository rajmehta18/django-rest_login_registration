from rest_framework import serializers
from .models import User
import base64
from django.conf import settings
import os


class UserSerializer(serializers.ModelSerializer):
    #password = make_password(validated_data['password'])
    class Meta:
        model=User
        fields = ['firstname','lastname','email','password']
    
# class favouriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['id','favourite']

