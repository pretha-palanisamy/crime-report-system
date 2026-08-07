from django.contrib import admin
from .models import Crime

@admin.register(Crime)
class CrimeAdmin(admin.ModelAdmin):
    list_display = ('crime_type', 'location','reported_by', 'status','date_reported')  # table la enna column varanum
    list_filter = ('status', 'crime_type')  # side la filter varum
    search_fields = ('location', 'description') # search box varum
    list_editable = ('status',)

# Register your models here.