from rest_framework import routers
from planner.viewsets import EventViewSet

router = routers.DefaultRouter()

router.register(r'event', EventViewSet)