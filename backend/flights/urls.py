from rest_framework.routers import DefaultRouter
from .views import FlightRequestViewSet, DestinationViewSet

router = DefaultRouter()
router.register(r'destinations', DestinationViewSet)
router.register(r'flights', FlightRequestViewSet)

urlpatterns = router.urls
