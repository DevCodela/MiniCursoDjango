from django import forms
from .models import Inscription


class InscriptionForm(forms.ModelForm):

	slug_course = forms.CharField(max_length=100, 
			widget = forms.TextInput(attrs = {
					'type' : 'text'
				}))

	class Meta:
		model = Inscription
		fields = ('full_name', 'email')
		widgets = {
			'full_name' : forms.TextInput(attrs = {
					'class' : 'mini_form__input',
					'type' : 'text',
					'placeholder' : 'Tu Nombre'
				}),
			'email' : forms.TextInput(attrs = {
					'class' : 'mini_form__input',
					'type' : 'email',
					'placeholder' : 'Tu Email'
				})
		}

	def clean(self):
		email = self.cleaned_data.get('email')
		slug_course = self.cleaned_data.get('slug_course')
		email_exist = Inscription.objects.filter(email = email,
							course__slug = slug_course).exists()
		if email_exist:
			self.add_error('email', 'Este email ya esta registrado en este curso')