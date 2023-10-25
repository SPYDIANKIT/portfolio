from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact_view, name='contact'),
    path('experience/',experience_view,name='experience'),
    path('download-resume/', download_resume, name='download_resume'),
    
]
