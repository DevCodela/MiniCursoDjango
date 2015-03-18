from django.contrib import admin
from .models import Course, Inscription

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	pass

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
	pass