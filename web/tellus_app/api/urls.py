"""
API urls
"""
from django.conf.urls import include
from rest_framework import routers
from django.urls import path

from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from api import views


class TellusView(routers.APIRootView):
    """
    Counted cars of all our permanent road counting apparatus.
    These consists of counted cars per hour per speed/type and are updated monthly.

    The code for this application is available from:
    - https://github.com/Amsterdam/tellus

    Note:

    These endpoints require authentication using the Employee login for example.
    """  # noqa


class TellusRouter(routers.DefaultRouter):
    APIRootView = TellusView


router = TellusRouter()


router.register(r'tellus', views.TellusViewSet)
router.register(r'lengtecategorie', views.LengteCategorieViewSet)

router.register(r'snelheidscategorie', views.SnelheidsCategorieViewSet)

router.register(r'tellusdata', views.TellusDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
