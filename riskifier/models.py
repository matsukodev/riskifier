from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class RiskifierData(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10)
    education = models.CharField(max_length=300)
    marital_status = models.CharField(max_length=20)
    children = models.PositiveSmallIntegerField()
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_industry = models.CharField(max_length=100)
    experience = models.PositiveSmallIntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            blank=True, null=True)

    def store(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
