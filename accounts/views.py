from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView

from .models import Client, Project


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project

    def get_success_url(self):
        return reverse('home')


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'time_spent', 'cost']
