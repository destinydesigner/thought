from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from things import views


router = DefaultRouter()
router.register(r'things', views.ThingViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
