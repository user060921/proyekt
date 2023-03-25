from django.db import models


class Article(models.Model):
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


