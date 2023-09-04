from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workoutcompmain import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'competitions', views.CompetitionViewSet,basename="competition")
router.register(r'workouts', views.WorkoutViewSet,basename="workout")
router.register(r'users', views.UserViewSet,basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]