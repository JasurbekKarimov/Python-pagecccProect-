from django.db import models
from django.urls import reverse
from django.db import models


class MyModel(models.Model):
    id = models.BigAutoField(primary_key=True)

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='backgrounds/')



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])