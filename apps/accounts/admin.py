from django.contrib import admin
from .models import User, Employer, Candidate

admin.site.register(User)
admin.site.register(Employer)
admin.site.register(Candidate)