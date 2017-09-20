from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from api import views

#
#  Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
#
schema_view = get_schema_view(
    title='Tellus API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)
router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs', schema_view, name='docs'),
    url(r'^tellus/$', views.TellusList.as_view(), name='tellus-list'),
    url(r'^tellus/(?P<pk>[0-9]+)/', views.TellusDetail.as_view(), name='tellus-detail'),
    url(r'^lengtecategorie/$', views.LengteCategorieList.as_view(), name='lengtecategorie-list'),
    url(r'^lengtecategorie/(?P<pk>[0-9]+)/', views.SnelheidsCategorieDetail.as_view(), name='lengtecategorie-detail'),
    url(r'^snelheidscategorie/$', views.LengteCategorieList.as_view(), name='snelheidcategorie-list'),
    url(r'^snelheidscategorie/(?P<pk>[0-9]+)/', views.SnelheidsCategorieDetail.as_view(),
        name='snelheidscategorie-detail'),
    url(r'^tellusdata/$', views.TellusDataList.as_view(), name='tellusdata-list'),
    url(r'^tellusdata/(?P<pk>[0-9]+)/$', views.TellusDataDetail.as_view(), name='tellusdata-detail'),
]
