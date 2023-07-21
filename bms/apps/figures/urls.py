from rest_framework import routers

from figures import views


router = routers.DefaultRouter()
router.register(r'figures',views.FigureViewSets)
urlpatterns = []
urlpatterns += router.urls