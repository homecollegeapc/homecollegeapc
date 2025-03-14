from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Default route for homepage
    path('contact/', views.contact, name='contact'),
     path('index/', views.index, name='index'),
     path('about/', views.about, name='about'), 
     path('programs/', views.programs, name='programs'),
     path("admission/", views.admission, name="admission"),
]
