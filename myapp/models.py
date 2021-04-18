from django.db import models
import datetime

# Create your models here.

class inputFields(models.Model) :
    country = models.CharField(max_length=100)
    environment = models.CharField(max_length=100)
    component = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    total = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s %s' % (self.total, self.component)
