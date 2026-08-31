from django.urls import path
from .views import JobListAPI, JobCreateAPI, HealthCheckAPI

urlpatterns = [
    path('jobs/', JobListAPI.as_view(), name='job-list'),
    path('jobs/create/', JobCreateAPI.as_view(), name='job-create'),
    path('health/', HealthCheckAPI.as_view(), name='health-check'),
]