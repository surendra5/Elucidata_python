from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    document = models.FileField(upload_to='documents/')

