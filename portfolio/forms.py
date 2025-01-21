from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import ContactFormSubmission, NewsletterSubscription, DataSolutionCategory

class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactFormSubmission
		fields = ['name', 'email', 'phone_number', 'category', 'message']
		widgets = {
			'name':forms.TextInput(attrs={'placeholder': 'Your name',}),
			'email':forms.EmailInput(attrs={'placeholder': 'Your email',}),
			'category': forms.Select(attrs={'class': 'form-control',}),
			'message': forms.Textarea(attrs={'rows': 6, 'placeholder':'Your message'}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Send Message'))
		self.fields['category'].queryset = DataSolutionCategory.objects.filter(is_visible=True)
		self.fields['category'].empty_label = 'What can we help with?'

class NewsletterSubscriptionForm(forms.ModelForm):
	class Meta:
		model = NewsletterSubscription
		fields = ['email']
		widgets = {
			'email': forms.EmailInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter your email address',
			}),
		}
		labels = {
			'email': '',  # No label for cleaner design
		}



