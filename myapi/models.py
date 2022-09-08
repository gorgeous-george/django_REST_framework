from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """
    Model representing a post.
    """
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


class Comment(models.Model):
    """
    Model representing a comment.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.text
