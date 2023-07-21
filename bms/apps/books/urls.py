from rest_framework import routers

from books import views


router = routers.DefaultRouter()
router.register(r'books',views.BookViewSets)
urlpatterns = []
urlpatterns += router.urls