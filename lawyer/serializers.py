from rest_framework import serializers
from django.contrib.auth.models import User
from .models import LawyerProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)
        return user


class LawyerProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  

    class Meta:
        model = LawyerProfile
        fields = [
            'id',
            'user',
            'mobile_number',
            'address',
            'bar_association_id',
            'specialization',
            'bio',
            'profile_picture',
            'website',
            'years_of_experience',
            'total_cases_handled',
            'languages_spoken',
            'rating',
            'is_verified',
            'joined_date',
            'last_active',
        ]
        read_only_fields = ['joined_date', 'last_active', 'is_verified']
