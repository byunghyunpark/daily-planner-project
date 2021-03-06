from django.db import models

class Schedule(models.Model):
    name = models.CharField(max_length=100)
    plan_start = models.DateTimeField(null=True, blank=True)
    plan_finish = models.DateTimeField(null=True, blank=True)
    real_start = models.DateTimeField(null=True, blank=True)
    real_finish = models.DateTimeField(null=True, blank=True)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
