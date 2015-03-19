from django.contrib import admin

from .models import Company, Client, Technology, Project


class BaseAccountAdmin(admin.ModelAdmin):

    exclude = (
        'created_at',
        'updated_at'
    )


class CompanyAdmin(BaseAccountAdmin):
    pass


class ClientAdmin(BaseAccountAdmin):
    pass


class TechnologyAdmin(BaseAccountAdmin):
    pass


class ProjectAdmin(BaseAccountAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Project, ProjectAdmin)
