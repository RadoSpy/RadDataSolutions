from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from urllib.parse import urlparse, urlunparse

from .models import DataSolutionCategory
from .forms import ContactForm
from .forms import NewsletterSubscriptionForm

site_keywords = ['Data Management', 'Analytics', 'Machine Learning', 'Cloud Solutions', 'ETL']
#nav_sections = {'Home':[], 'What We Do':[], 'How We Do It':[], 'About Us':[], 'Services':[dynamic]}

GLOBAL_PRESETS = {
	'name_full': 'Rad Data Solutions',
	'name_camel': 'RadDataSolutions',
	'name_short': 'RDS',
	'site_title': 'Rad Data Solutions - Your Data Partner',
	'site_description': 'Expert solutions for your data challenges, from storage to AI.',
	'site_keywords': ', '.join(site_keywords),
	'contact_email': 'hello@raddatasolutions.com',
	'contact_phone': '+44 7934747759',
	'address_1': 'London',
	'address_2': 'United Kingdom',
	'address_full': 'London, United Kingdom',
	'social_links': {
		'facebook': 'https://facebook.com/raddatasolutions',
		'linkedin': 'https://linkedin.com/company/raddatasolutions',
		},
	}

# All categories from DB - these need to be setup first when deploying
categories = DataSolutionCategory.objects.filter(is_visible=True)

# The home screen of entire page
def home(request):

	# Create Context
	context = {
		'categories': categories,
		**GLOBAL_PRESETS, 
	}
	return render(request, 'index.html', context)

# Service detail is for handling of sub-pages that showcase each service
def service_detail(request, href):
	# Create Context
	category = get_object_or_404(DataSolutionCategory, href=href, is_visible=True)

	service_sections = category.service_sections.all()  # Get service sections data
	service_header = service_sections.filter(section_type__name="header").first()
	service_desc = service_sections.filter(section_type__name="desc").first()
	service_about_img_path = service_sections.filter(section_type__name="about_img_path").first()
	service_discover_img_path = service_sections.filter(section_type__name="discover_img_path").first()
	service_example_solutions = service_sections.filter(section_type__name="example_solution")
	service_subcategories = service_sections.filter(section_type__name="service_subcategory")

	context = {
		'category': category,
		'categories': categories,
		'service_header':service_header,
		'service_desc':service_desc,
		'service_about_img_path':service_about_img_path,
		'service_discover_img_path':service_discover_img_path,
		'service_example_solutions':service_example_solutions,
		'service_subcategories':service_subcategories,

		**GLOBAL_PRESETS,
	}
	return render(request, 'service_detail.html', context)


# Contact us page - for generating leads/customers - most of the page redirects here
# Includes POST for saving customers
def contact_us(request):
	extra_tags='contact_form'
	# Post Handling
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			success_message = "Your message has been sent successfully!"
			messages.add_message(request, messages.SUCCESS, success_message, extra_tags=extra_tags)

			# Redirect
			#return render(request, 'contact_success.html', {'name': 'test'})
		else:
			error_message = 'There was an issue with your submission. Please check the errors below.'
			messages.add_message(request, messages.ERROR, error_message, extra_tags=extra_tags)
	else:
		form = ContactForm()
		

	# Create Context
	context = {
		'categories': categories,
		**GLOBAL_PRESETS, 
		'form': form,
	}

	return render(request, 'contact_us.html', context)


# About

# The team
def about_team(request):
	context = {
		'categories': categories,
		**GLOBAL_PRESETS, 
	}
	return render(request, 'about_team.html', context)

# Blog testing context
articles = [{
			'service':'Automation',
			'title':'Business Automation Ideas to Save Time and Money',
			'desc':'Find out more about practical examples of where automation can help you save time and money',
			'img_static_path':'hero-bg.jpg',
			'created':'13/01/2025'
			},
			{
			'service':'BI & Analytics',
			'title':'Ways Business Intelligence Can Transform Your Data Into Insights',
			'desc':'With automated data flows behind the scenes and regular refreshes you will be always able to see how your business is doing, acting on opportunities and issues as they arise.',
			'img_static_path':'subservices/automation_discover.jpg',
			'created':'28/01/2025'
			},
			{
			'service':'Data Strategy',
			'title':'Data Strategy for Small Businesses – Key Components',
			'desc':'Find out more about what it is and why it is important.',
			'img_static_path':'subservices/ai_solutions_about.jpg',
			'created':'13/02/2025'
			}
			]

# The blog
def blog(request):
	context = {
		'categories': categories,
		**GLOBAL_PRESETS, 
		'articles':articles
	}
	return render(request, 'blog.html', context)


######################################## BELOW SECTION IS FOR CROSS PAGE UTILS ####################################

# signup handler for multiple pages
def newsletter_signup(request):
	extra_tags = 'newsletter'
	if request.method == 'POST':
		form = NewsletterSubscriptionForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Thank you for signing up!", extra_tags=extra_tags)
		else:
			error_message = 'There was an error. Please check your email and try again.'
			messages.add_message(request, messages.ERROR, error_message, extra_tags=extra_tags)
			
		referer = request.META.get('HTTP_REFERER', '/')
		url_parts = urlparse(referer)
		updated_url = urlunparse(url_parts._replace(fragment='footer'))

		return redirect(updated_url)


