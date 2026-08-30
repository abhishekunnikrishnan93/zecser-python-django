from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('candidate', 'Candidate'),
        ('admin', 'Admin'),
    ]
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    company_size = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name