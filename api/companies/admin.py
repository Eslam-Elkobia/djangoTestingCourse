from django.contrib import admin

from api.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'last_update', 'application_link', 'notes')
    list_display_links = ('id', 'name')  # choose fields that needed to be clickable to show item details
    list_filter = ('status', 'last_update', 'name')
    list_editable = ('status',)
    list_per_page = 25
    search_fields = ('name',)
    date_hierarchy = 'last_update'
    ordering = ('name', 'status', 'last_update')


