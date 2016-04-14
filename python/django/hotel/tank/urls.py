from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^room/(?P<room_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^add_reservation/', views.add_reservation, name='add_reservation'),
        url(r'^add_visitor/', views.add_visitor, name='add_visitor'),
        url(r'^success/', views.success, name='success'),
        url(r'^failed/', views.failed, name='failed'),
        ]
