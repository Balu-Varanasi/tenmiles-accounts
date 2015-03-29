"""

Models in 'accounts':

    1. Company
    2. Client
    3. Technology
    4. Project

"""

from decimal import Decimal

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    """
    Companies within the 'accounts' are represented by this model.

    name is required. Other fields are optional.
    """

    name = models.CharField(
        _("Name"),
        max_length=50)

    description = models.CharField(
        _("Description"),
        max_length=500,
        null=True,
        blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("company_detail",
                       args=[self.pk])


class Client(models.Model):
    """
    Clients within the 'accounts' are represented by this model.

    name is required. Other fields are optional.
    """

    name = models.CharField(
        _("Name"),
        max_length=50)

    email = models.EmailField(
        _("Email"))

    company = models.ForeignKey(
        "accounts.Company")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("technology_detail",
                       args=[self.pk])


class Technology(models.Model):
    """
    Technologies within the 'accounts' are represented by this model.

    name is required. Other fields are optional.
    """
    name = models.CharField(
        _("Name"),
        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("technology_detail",
                       args=[self.pk])


class DailySprintTimeSpan(models.Model):
    """
    DailySprintTimeSpan within the 'accounts' are represented by this model.

    all fields are required.
    """

    project = models.ForeignKey(
        "accounts.Project")

    started_at = models.DateTimeField(
        _("Started At"),
        null=True)

    ended_at = models.DateTimeField(
        _("Ended At"),
        null=True)

    hours_spent = models.DecimalField(
        _("Time Spent"),
        max_digits=5,
        decimal_places=2,
        default=Decimal(0))

    def save(self, *args, **kwargs):
        date_delta = self.ended_at - self.started_at
        self.hours_spent += Decimal(date_delta.total_seconds() / 3600)
        super(DailySprintTimeSpan, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("daily_sprint_detail",
                       args=[self.pk])


class ProjectStatistics(models.Model):
    """
    DailySprintTimeSpan within the 'accounts' are represented by this model.

    all fields are required.
    """

    project = models.OneToOneField(
        "accounts.Project")

    total_time_spent = models.DecimalField(
        _("Time Spent"),
        max_digits=50,
        decimal_places=10,
        default=Decimal(0))

    total_cost = models.DecimalField(
        _("Time Spent"),
        max_digits=50,
        decimal_places=10,
        default=Decimal(0))

    class Meta:
        verbose_name = "Project Statistics"
        verbose_name_plural = "Projects Statistics"

    def __str__(self):
        return self.project.name

    def get_total_hours(self):
        return self.total_time_spent

    def get_total_cost(self):
        return self.total_cost


class Project(models.Model):
    """
    Projects within the 'accounts' are represented by this model.

    name is required. Other fields are optional.
    """

    client = models.ForeignKey(
        "accounts.Client")

    name = models.CharField(
        _("Name"),
        max_length=50)

    technologies = models.ManyToManyField(
        "accounts.Technology")

    start_date = models.DateField(
        _("Start Date"),
        null=True)

    end_date = models.DateField(
        _("End Date"),
        null=True)

    cost = models.DecimalField(
        _("Cost Per Hour"),
        max_digits=5,
        decimal_places=2,
        default=Decimal(0))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        ProjectStatistics.objects.get_or_create(
            project=self)

    def get_absolute_url(self):
        return reverse("project_detail",
                       args=[self.pk])

    def get_total_cost(self):
        project_statistics, created = ProjectStatistics.objects.get_or_create(
            project=self)
        return project_statistics.get_total_cost()

    def get_total_hours(self):
        project_statistics, created = ProjectStatistics.objects.get_or_create(
            project=self)
        return project_statistics.get_total_hours()
