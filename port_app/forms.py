from django import forms
from .models import Contact
class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone', max_length=15, required=False)
    subject = forms.CharField(label='Subject', max_length=200)
    message = forms.CharField(label='Message', widget=forms.Textarea)