from django.urls import include, path
from rest_framework import routers

from challenge.views import LabelViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"labels", LabelViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
