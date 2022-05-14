from django.contrib import admin

# Register your models here.
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','course_name','email']