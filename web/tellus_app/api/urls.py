from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from .views import TellusDataViewSet, TellusViewSet, LengteCategorieViewSet, SnelheidsCategorieViewSet

router = routers.DefaultRouter()
router.register(r'tellus', TellusViewSet)
router.register(r'lengtecategorie', LengteCategorieViewSet)
router.register(r'snelheidscategorie', SnelheidsCategorieViewSet)
router.register(r'tellus_data', TellusDataViewSet)

#
#  Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
#
schema_view = get_schema_view(
    title='Tellus API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

urlpatterns = [
    url('^docs', schema_view, name='docs'),
    url(r'^', include(router.urls)),
]
