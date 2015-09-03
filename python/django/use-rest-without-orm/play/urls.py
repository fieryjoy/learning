from los import views
from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'los', views.LOList, base_name="los")

urlpatterns = patterns(
    '',
    url(r'', include(router.urls)),
    url(r'^los/$', views.LOList.as_view(), name='los-list'),
    url(r'^los/(?P<pk>[0-9]+)/$', views.LODetail.as_view()),
)
