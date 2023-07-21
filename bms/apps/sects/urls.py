from sects import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'sects',views.SectViewSet)


urlpatterns = []
urlpatterns += router.urls