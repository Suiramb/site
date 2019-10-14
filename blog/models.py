from django.db import models


class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimespamtedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255, default="Anonyme")
    image_url = models.CharField(max_length=255, default="")
    image_alt = models.CharField(max_length=50, default="Image")

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    fake_info = models.PositiveIntegerField(default=0)
    verified_info = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

# Create your models here.
