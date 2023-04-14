from django.db import models
from django.conf import settings

class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
    
