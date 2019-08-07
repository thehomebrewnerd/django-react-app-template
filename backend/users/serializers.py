from rest_framework import serializers

from users import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a UserProfile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'fname', 'lname', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            fname=validated_data['fname'],
            lname=validated_data['lname'],
            password=validated_data['password']
        )

        return user
