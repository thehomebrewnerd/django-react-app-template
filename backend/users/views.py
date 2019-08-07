from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication

from users import models, permissions, serializers


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating UserProfile objects"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('email', 'fname', 'lname')
