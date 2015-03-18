from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

from .models import Course

# Create your views here.

class HomeView(TemplateView):

	template_name = 'home.html'

class CourseDetailView(DetailView):

	model = Course
	template_name = 'course_detail.html'
	context_object_name = 'course'