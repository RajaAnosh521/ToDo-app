from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False) 
    description = models.TextField(blank=True, null=True) 
    date = models.DateTimeField(blank=False) 
    completed = models.BooleanField(default=False) 

    def __str__(self):
        return self.title 
