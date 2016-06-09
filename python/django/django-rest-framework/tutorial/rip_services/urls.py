from django.conf.urls import url
from rip_services import views

urlpatterns = [
    url(r'^ripcreationrequests/$', views.ripcreationrequest_list),
    url(r'^ripcreationrequests/(?P<pk>[0-9]+)/$', views.ripcreationrequest_detail),
]