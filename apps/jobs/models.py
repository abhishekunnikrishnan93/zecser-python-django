from django.db import models
from apps.accounts.models import Employer, Candidate
class Job(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('draft', 'Draft'),
    ]
    employer = models.ForeignKey(Employer, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    salary_range = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('screening', 'Screening'),
        ('ai_interview', 'AI Interview'),
        ('assessment', 'Assessment'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    resume_snapshot = models.FileField(upload_to='application_resumes/', blank=True, null=True)
    class Meta:
        unique_together = ('candidate', 'job')
    def __str__(self):
        return f"{self.candidate.full_name} → {self.job.title}"