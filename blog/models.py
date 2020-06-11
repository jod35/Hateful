from django.db import models

# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=25)
    title=models.CharField(max_length=40)
    message=models.TextField()
    date_created=models.DateField(auto_now=True)

    def __str__(self):
        return self.name