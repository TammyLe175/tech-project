from django.db import models

# Create your models here.
class App(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=100)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.task