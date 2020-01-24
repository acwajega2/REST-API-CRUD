from django.db import models

# Create your models here.
class Cake(models.Model):
    
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title
    @property
    def owner(self):
        return self.user