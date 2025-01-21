from django.contrib import admin
from .models import DataSolutionCategory, ServiceSection, ServiceSectionType
from .models import ContactFormSubmission, NewsletterSubscription

@admin.register(DataSolutionCategory)
class DataSolutionCategoryAdmin(admin.ModelAdmin):
	#list_display = ('name', 'desc')
	list_filter = ('is_visible',)

	def get_absolute_url(self, obj):
		return f'<a href="{obj.get_absolute_url()}">View</a>'
	get_absolute_url.allow_tags = True

@admin.register(ServiceSectionType)
class ServiceSectionTypeAdmin(admin.ModelAdmin):
	pass

@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
	list_filter = ('service','section_type',)


@admin.register(ContactFormSubmission)
class ContactFormSubmissionAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'category', 'message')
	list_filter = ('category',)

@admin.register(NewsletterSubscription)
class ContactFormSubmissionAdmin(admin.ModelAdmin):
	list_display = ('email', 'subscribed_on',)
	list_filter = ('subscribed_on',)



