from rest_framework import routers

from scholars.views import ScholarViewSet


router = routers.DefaultRouter()
router.register(r'scholars',ScholarViewSet)
urlpatterns = []
urlpatterns += router.urls