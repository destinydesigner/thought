from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Thing(models.Model):
    description = models.CharField(max_length=256)

    def __unicode__(self):
        return "%s(%s)" % (self.description, self.id)
