from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete


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


class DepartmentInfomation(models.Model):
    title = models.CharField(max_length=100)
    info_1 = models.CharField(max_length=100)
    info_2 = models.CharField(max_length=100)
    info = models.OneToOneField(Department, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'polls_department_info'


@receiver(post_delete, sender=DepartmentInfomation)
def post_delete_info(sender, instance, *args, **kwargs):
    if instance.info:  # just in case user is not specified
        instance.info.delete()


class City(models.Model):
    """
    model test for field created auto_now_add=True
    """
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
