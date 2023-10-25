from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.subject}'
    



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    date_completed = models.DateField()

    def __str__(self):
        return self.title