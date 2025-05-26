from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'major', 'grade']

admin.site.register(Student, StudentAdmin)