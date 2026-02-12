from django.contrib import admin

from .models import Classroom

# Register your models here.
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')

    list_filter = ('created_at', 'updated_at')

    search_fields = ('name', 'description')

admin.site.register(Classroom, ClassroomAdmin)