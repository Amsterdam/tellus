"""
API urls
"""
from django.conf.urls import include
from rest_framework import routers
from django.urls import path

from api import views


class TellusView(routers.APIRootView):
    """
    Counted cars of all our permanent road counting apparatus.
    These consists of counted cars per hour per speed/type and are updated monthly.

    The code for this application is available from:
    - https://github.com/Amsterdam/tellus

    Note:

    The actual telling and aggregate endpoints require authentication using the Employee login.
    """
    pass


class TellusRouter(routers.DefaultRouter):
    APIRootView = TellusView


router = TellusRouter()

router.register(r'meetlocatie', views.MeetlocatieViewSet)
router.register(r'lengte_interval', views.LengteIntervalViewSet)
router.register(r'snelheids_interval', views.SnelheidsIntervalViewSet)
router.register(r'snelheids_categorie', views.SnelheidsCategorieViewSet)
router.register(r'representatief_categorie', views.RepresentatiefCategorieViewSet)
router.register(r'validatie_categorie', views.ValidatieCategorieViewSet)
router.register(r'meetraai_categorie', views.MeetraaiCategorieViewSet)
router.register(r'tellus', views.TellusViewSet)
router.register(r'tel_richting', views.TelRichtingViewSet)
router.register(r'telling', views.TellingViewSet)
router.register(r'telling_totaal_uur_dag', views.TellusDataCarsPerHourPerDayViewSet)
router.register(r'telling_totaal_uur_lengte_dag', views.TellusDataCarsPerHourLengthViewSet)
router.register(r'telling_totaal_uur_snelheid_dag', views.TellusDataCarsPerHourSpeedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
