from django.conf.urls import patterns, url

from .views import (
    ClientListView, ClientDetailView, ProjectUpdateView,
    ProjectDetailView, ProjectListView)


urlpatterns = patterns(
    '',

    url(r'^clients/$',
        ClientListView.as_view(), name="client_list"),

    url(r'^projects/$',
        ProjectListView.as_view(), name="project_list"),

    url(r'^clients/(?P<pk>\d+)/$',
        ClientDetailView.as_view(), name="client"),

    url(r'^$', ClientListView.as_view(), name="home"),

    url(r'^projects/(?P<pk>\d+)/edit/$',
        ProjectUpdateView.as_view(), name="project_edit"),

    url(r'^projects/(?P<pk>\d+)/$',
        ProjectDetailView.as_view(), name="project_detail"),
)
