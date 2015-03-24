from django.conf.urls import patterns, url

from .views import (

    CompanyListView, CompanyDetailView, CompanyCreateView,
    CompanyUpdateView, CompanyDeleteView,

    ClientListView, ClientDetailView, ClientCreateView,
    ClientUpdateView, ClientDeleteView,

    ProjectListView, ProjectDetailView, ProjectCreateView,
    ProjectUpdateView, ProjectDeleteView,

    TechnologyListView, TechnologyDetailView, TechnologyCreateView,
    TechnologyUpdateView, TechnologyDeleteView,

    HomeView,)


###########################################################
#                       Client URLs                       #
###########################################################

urlpatterns = patterns(
    '',

    url(r'^clients/$',
        ClientListView.as_view(), name="client_list"),

    url(r'^clients/new/$',
        ClientCreateView.as_view(), name="client_new"),


    url(r'^clients/(?P<pk>\d+)/edit/$',
        ClientUpdateView.as_view(), name="client_edit"),

    url(r'^clients/(?P<pk>\d+)/$',
        ClientDetailView.as_view(), name="client_detail"),

    url(r'^clients/(?P<pk>\d+)/delete/$',
        ClientDeleteView.as_view(), name="client_delete"),

)


###########################################################
#                       Companies URLs                       #
###########################################################

urlpatterns += patterns(
    '',

    url(r'^companies/$',
        CompanyListView.as_view(), name="company_list"),

    url(r'^companies/new/$',
        CompanyCreateView.as_view(), name="company_new"),


    url(r'^companies/(?P<pk>\d+)/edit/$',
        CompanyUpdateView.as_view(), name="company_edit"),

    url(r'^companies/(?P<pk>\d+)/$',
        CompanyDetailView.as_view(), name="company_detail"),

    url(r'^companies/(?P<pk>\d+)/delete/$',
        CompanyDeleteView.as_view(), name="company_delete"),

)


###########################################################
#                       Projects URLs                     #
###########################################################

urlpatterns += patterns(
    '',

    url(r'^projects/$',
        ProjectListView.as_view(), name="project_list"),

    url(r'^projects/new/$',
        ProjectCreateView.as_view(), name="project_new"),

    url(r'^projects/(?P<pk>\d+)/edit/$',
        ProjectUpdateView.as_view(), name="project_edit"),

    url(r'^projects/(?P<pk>\d+)/$',
        ProjectDetailView.as_view(), name="project_detail"),

    url(r'^projects/(?P<pk>\d+)/delete/$',
        ProjectDeleteView.as_view(), name="project_delete"),
)

###########################################################
#                       Technology URLs                   #
###########################################################

urlpatterns += patterns(
    '',

    url(r'^technologies/$',
        TechnologyListView.as_view(), name="technology_list"),

    url(r'^technologies/new/$',
        TechnologyCreateView.as_view(), name="technology_new"),

    url(r'^technologies/(?P<pk>\d+)/edit/$',
        TechnologyUpdateView.as_view(), name="technology_edit"),

    url(r'^technologies/(?P<pk>\d+)/$',
        TechnologyDetailView.as_view(), name="technology_detail"),

    url(r'^technologies/(?P<pk>\d+)/delete/$',
        TechnologyDeleteView.as_view(), name="technology_delete"),
)

###########################################################
#                       Home URLs                         #
###########################################################

urlpatterns += patterns(
    '',
    url(r'^$', HomeView.as_view(), name="home"),
)
