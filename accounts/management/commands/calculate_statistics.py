from decimal import Decimal

from django.core.management.base import BaseCommand

from accounts.models import Project, DailySprintTimeSpan, ProjectStatistics


class Command(BaseCommand):
    args = 'no aguments'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        for project in Project.objects.all():

            project_statistics, created = \
                ProjectStatistics.objects.get_or_create(
                    project=project)

            total_time = Decimal(0)
            total_cost = Decimal(0)
            for daily_sprint in DailySprintTimeSpan.objects.filter(
                    project=project):

                total_time += daily_sprint.hours_spent
                total_cost += daily_sprint.hours_spent * project.cost

            project_statistics.total_time_spent = total_time
            project_statistics.total_cost = total_cost
            project_statistics.save()

            self.stdout.write(
                'Successfully calculated statistics for project "%s"'
                % project.name)
