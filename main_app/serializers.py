from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", 'username', 'password']
#         extra_kwargs = {"password": {"write_only": True}}
        
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
    
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', "date_added", "user"]
#         extra_kwargs = {"user": {"read_only": True}}

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'thumbnail', 
                    'status', 'format', 'start_date', 'finish_date', 
                    'genre', 'publication_year', 'total_pages', 'total_time', 're_read']