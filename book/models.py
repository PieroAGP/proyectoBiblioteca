from django.db import models
#para la fecha
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.IntegerField()
    synopsys = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title
