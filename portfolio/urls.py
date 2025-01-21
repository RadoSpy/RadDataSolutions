from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('services/<str:href>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact_us, name='contact_us'),
    path('team/', views.about_team, name='about_team'),
    path('blog/', views.blog, name='blog'),

    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
]