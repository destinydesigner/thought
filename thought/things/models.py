from __future__ import unicode_literals
from django.db import models


class Thing(models.Model):
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        default=None, null=True)
    description = models.CharField(max_length=256)
    group_root = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='members',
        default=None, null=True)

    def __unicode__(self):
        return "%s(%s)" % (self.description, self.id)
