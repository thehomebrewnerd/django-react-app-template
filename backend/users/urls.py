from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewset)
router.register('feed', views.UserProfileFeedItemViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginAPIView.as_view()),
]
