import uuid
from django.db import models

# Create your models here.

class MessageData(models.Model):
    message = models.CharField(max_length = 1000)
    decoded = models.CharField(max_length = 1000)
    ID = models.AutoField(primary_key=True)

    def __str__(self):
        template = '{0.message}, {0.decoded}'
        return template.format(self)

