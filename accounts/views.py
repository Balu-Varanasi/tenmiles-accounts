from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    UpdateView, CreateView, DeleteView)

from .models import Company, Client, Project, Technology


###########################################################
#                       Company                           #
###########################################################

class CompanyListView(ListView):
    model = Company
    template_name = 'companies/company_list.html'


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'companies/company_form.html'
    success_url = reverse_lazy('company_list')


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'companies/company_detail.html'


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'description']


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'companies/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')


###########################################################
#                       Clients                          #
###########################################################

class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'


class ClientCreateView(CreateView):
    model = Client
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('client_list')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'company']


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')


###########################################################
#                       Projects                          #
###########################################################

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'client', 'technologies', 'time_spent',
              'cost', 'start_date']


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


###########################################################
#                       Technology                          #
###########################################################

class TechnologyListView(ListView):
    model = Technology
    template_name = 'technologies/technology_list.html'


class TechnologyCreateView(CreateView):
    model = Technology
    template_name = 'technologies/technology_form.html'
    success_url = reverse_lazy('technology_list')


class TechnologyDetailView(DetailView):
    model = Technology
    template_name = 'technologies/technology_detail.html'


class TechnologyUpdateView(UpdateView):
    model = Technology
    template_name = 'technologies/technology_form.html'
    fields = ['name']


class TechnologyDeleteView(DeleteView):
    model = Technology
    template_name = 'technologies/technology_confirm_delete.html'
    success_url = reverse_lazy('technology_list')


###########################################################
#                       Home                          #
###########################################################

class HomeView(ListView):
    model = Client
    template_name = 'accounts/home.html'
