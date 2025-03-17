from django.db import models

# Create your models here.
class App(models.Model):
    status_options = [
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=50)
    task_description = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=status_options, default="in-progress")

    def __str__(self):
        return self.task, self.name
