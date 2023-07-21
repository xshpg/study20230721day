from rest_framework import routers

from martails import views

router = routers.DefaultRouter()
router.register(r'martails',views.MartailsViewSets)
urlpatterns = []
urlpatterns += router.urls