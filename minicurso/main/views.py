from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

from .models import Course
from .forms import InscriptionForm

# Create your views here.

class HomeView(TemplateView):

	template_name = 'home.html'

class CourseDetailView(DetailView):

	model = Course
	template_name = 'course_detail.html'
	context_object_name = 'course'

	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		context['form'] = InscriptionForm()
		return context

	def post(self, request, *args, **kwargs):
		form = InscriptionForm(request.POST.copy())
		form.instance.course = self.get_object()
		form.data['slug_course'] = self.get_object().slug
		registered = False
		if form.is_valid():
			form.save()
			registered = True
		return render(request, 'course_detail.html', 
			{'form' : form, 'registered':registered, 'course':self.get_object() })