from django.db import models
from django.conf import settings

class Sesame(models.Model):
    def __str__(self):
        return self.owner.__str__() + ": " + self.name.__str__()

    # its owner
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # user named name
    name = models.CharField(max_length=256)

    # auth token
    auth_token = models.CharField(max_length=76)
