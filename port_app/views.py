# imports
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.http import FileResponse
from django.templatetags.static import static
import os
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def portfolio_view(request):
    return render(request, 'portfolio.html')

def experience_view(request):
    return render(request, 'experience.html')

def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save the data to the database
            contact_message = ContactMessage(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            contact_message.save()
            send_applicant_confirmation_email(first_name, email)

            # Redirect to the success page
            return render(request, 'success.html')

    return render(request, 'contact_form.html', {'form': form})


def send_applicant_confirmation_email(first_name, email):
    # Your email sending logic
    # Use Django's send_mail function
    send_mail(
        'Thank You for Contacting Us!',
        f'Dear {first_name},\n\nThank you for contacting us. We have received your message and will get back to you shortly.\n\nBest regards,\nYour Company Name',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )


def experience_view(request):
    projects = Project.objects.all()
    return render(request, 'experience.html', {'projects': projects})



from django.http import FileResponse

def download_resume(request):
    resume_path = os.path.join(settings.STATIC_ROOT, 'resume.pdf')
    
    response = FileResponse(open(resume_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'
    
    return response
