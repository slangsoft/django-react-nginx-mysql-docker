from django.db import models


class Todo(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title