from rest_framework import routers

from editors import views


router = routers.DefaultRouter()
router.register(r'editors',views.EditorViewSet)
urlpatterns = []
urlpatterns += router.urls