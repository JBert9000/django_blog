from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #auto_now_add=True sets the time to when this post was created and cannot be changed.

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # User model class is the foreign key for Post model class.

    # on_delete=models.CASCADE tells Django that when an author is deleted, their posts are deleted as well.

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
