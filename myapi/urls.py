from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapi import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename="posts")
router.register(r'comments', views.CommentViewSet, basename="comments")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
