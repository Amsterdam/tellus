"""
API urls and schema generator
"""
from django.conf.urls import include, url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from django.urls import path

from api import views


schema_view = get_schema_view(
    openapi.Info(
        title="Tellus API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


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

urlpatterns = [
    path('', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
