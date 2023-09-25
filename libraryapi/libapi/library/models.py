from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.title
