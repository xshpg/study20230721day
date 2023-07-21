from rest_framework import routers

from press import views

router = routers.DefaultRouter()
router.register(r'press',views.PressViewSet)
urlpatterns = []
urlpatterns += router.urls