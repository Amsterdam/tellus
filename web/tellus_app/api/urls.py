from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path

from api import views


class TellusView(routers.APIRootView):
    """
    List Signals and their related information.

    These API endpoints are part of the Signalen Informatievoorziening Amsterdam
    (SIA) application. SIA can be used by citizens and interested parties to inform
    the Amsterdam municipality of problems in public spaces (like noise complaints,
    broken street lights etc.) These signals (signalen in Dutch) are then followed
    up on by the appropriate municipal services.

    The code for this application (and associated web front-end) is available from:
    - https://github.com/Amsterdam/signals
    - https://github.com/Amsterdam/signals-frontend

    Note:
    Most of these endpoints require authentication. The only fully public endpoint
    is /signals/signal where new signals can be POSTed.
    """


class TellusRouter(routers.DefaultRouter):
    APIRootView = TellusView


router = TellusRouter()


router.register(r'^tellus', views.TellusViewSet)
router.register(r'^lengtecategorie', views.LengteCategorieViewSet)

router.register(r'^snelheidscategorie', views.LengteCategorieViewSet)

router.register(r'^tellusdata', views.TellusDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
