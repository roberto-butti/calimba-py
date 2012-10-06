from django.db import models
import datetime
from django.utils import timezone


class ActivityStatus(models.Model):

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=200)


class Activity(models.Model):

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_start = models.DateTimeField('date start activity')
    date_end = models.DateTimeField('date end activity')
    pub_date = models.DateTimeField('date published')
    status = models.ForeignKey(ActivityStatus)

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
