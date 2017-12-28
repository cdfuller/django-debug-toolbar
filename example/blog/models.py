from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.title
