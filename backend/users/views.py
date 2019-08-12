from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from users import models, permissions, serializers


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating UserProfile objects"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    filter_backends = (filters.SearchFilter, )
    search_fields = ('email', 'fname', 'lname')


class UserLoginAPIView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedItemViewset(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)