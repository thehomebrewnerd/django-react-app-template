from rest_framework import viewsets

from users import models, serializers


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating UserProfile objects"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
