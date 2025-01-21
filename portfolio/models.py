from django.db import models
from django.urls import reverse

class DataSolutionCategory(models.Model):
	CATEGORY_CHOICES = [
		('DM', 'Data Strategy & Management'),
		('DE', 'Data Integration & Automation'),
		('DA', 'Business Insights & Analytics'),
		('DS', 'Machine Learning & AI'),
		('SP', 'Data Security & Privacy'),
		('CD', 'Cloud Data Solutions'),
		('OT', 'Other Services'),  # For any other category
		('WD', 'Web Design'),
	]

	id = models.AutoField(primary_key=True) # Auto-generated ID (hidden by default) 
	code = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default='OT',)
	name = models.CharField(max_length=100, blank=True, null=True)
	name_full = models.CharField(max_length=255, blank=True, null=True)
	name_alternate = models.CharField(max_length=255, blank=True, null=True)
	desc = models.TextField(blank=True, null=True)  # Optional description of the category
	desc_oneliner = models.CharField(max_length=255, blank=True, null=True)
	desc_short = models.CharField(max_length=500, blank=True, null=True)
	bg_img_path = models.CharField(max_length=255, blank=True, null=True)
	bi_icon = models.CharField(max_length=255, blank=True, null=True)
	href = models.CharField(max_length=255, blank=True, null=True)
	is_visible = models.BooleanField(default=True)

	def __str__(self):
		return dict(self.CATEGORY_CHOICES).get(self.code, 'Unknown')

	def get_absolute_url(self):
		return reverse('service_detail', kwargs={'href': self.href})

	class Meta:
		verbose_name = "Data Solution Category"
		verbose_name_plural = "Data Solution Categories"

class ServiceSectionType(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, unique=True)
	desc = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name

class ServiceSection(models.Model):
	service = models.ForeignKey(DataSolutionCategory, related_name="service_sections", on_delete=models.CASCADE)
	section_type = models.ForeignKey(ServiceSectionType, on_delete=models.CASCADE)
	content = models.TextField()
	content_desc = models.TextField(blank=True, null=True)
	icon = models.CharField(max_length=50, blank=True, null=True)


	def __str__(self):
		if self.section_type.name=='example_solution' or self.section_type.name=='service_subcategory':
			return f"{self.service.name} - {self.section_type.name} - {self.content}"
		else:
			return f"{self.service.name} - {self.section_type.name}"

class ContactFormSubmission(models.Model):
	# ID
	id = models.AutoField(primary_key=True) # Auto-generated ID (hidden by default) 

	name = models.CharField(max_length=100) # Name of person contacting
	email = models.EmailField()  # User's email (required)
	phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number

	category = models.ForeignKey(
		DataSolutionCategory, 
		on_delete=models.SET_NULL, 
		null=True, 
		blank=True, 
		related_name='submissions'
	)

	message = models.TextField()  # Message from the user

	def __str__(self):
		return f"Message from {self.name}"
	class Meta:
		verbose_name = "Contact Form Submission"
		verbose_name_plural = "Contact Form Submissions"


class NewsletterSubscription(models.Model):
	email = models.EmailField(unique=True)  # Ensures each email is recorded only once
	subscribed_on = models.DateTimeField(auto_now_add=True)  # Timestamp for when the subscription occurred

	def __str__(self):
		return self.email
