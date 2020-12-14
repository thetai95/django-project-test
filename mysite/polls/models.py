from django.db import models


class Department(models.Model):
    """
    test datatables
    """
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'polls_department'
