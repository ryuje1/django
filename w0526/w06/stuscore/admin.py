from django.contrib import admin
from stuscore.models import Stuscore

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'total', 'avg']

admin.site.register(Stuscore, StudentAdmin)
