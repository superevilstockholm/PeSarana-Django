from django.contrib import admin

from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nisn', 'name', 'dob', 'classroom__name', 'created_at', 'updated_at')

    list_filter = ('classroom', 'dob', 'created_at', 'updated_at')

    search_fields = ('nisn', 'name', 'classroom__name')

admin.site.register(Student, StudentAdmin)