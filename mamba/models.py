from django.db import models

# Create your models here.
class FakeModel(models.Model):
    created_on = models.DateTimeField("date created", auto_now_add=True)
