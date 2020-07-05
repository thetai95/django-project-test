from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, blank=False)
    summary = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'link',)
