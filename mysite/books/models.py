from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        function này để khi mà create thành công thì redirect to url 'book_edit'
        """
        return reverse('book_edit', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'tbl_books'
