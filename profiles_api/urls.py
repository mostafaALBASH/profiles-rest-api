from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)
router.register('is-authenticated', views.HelloViewSet, base_name='is-authenticated')
router.register('api-token-auth', views.HelloViewSet, base_name='api-token-auth')
router.register('hello-view', views.HelloViewSet, base_name='hello-view')
# router.register('authenticate', views.HelloViewSet, base_name='authenticate')

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'^is-authenticated/', views.IsAuthenticated.as_view()),
    url(r'^api-token-auth/', views.CustomAuthToken.as_view()),
    # url(r'^authenticate/', views.CustomObtainAuthToken.as_view()),
    url(r'', include(router.urls))
]
