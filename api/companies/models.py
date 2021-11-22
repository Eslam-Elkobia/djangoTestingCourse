from django.db import models
from django.db.models import URLField
from django.utils.timezone import now


class Company(models.Model):
    CompanyStatus = (
        ('LAYOFFS', 'Layoffs'),
        ('HIRING_FREEZE', 'Hiring Freeze'),
        ('HIRING', 'Hiring'),
    )
    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(choices=CompanyStatus, default=CompanyStatus[2], max_length=30)
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)
