# Generated by Django 3.0.8 on 2021-01-20 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20201229_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentInfomation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info_1', models.CharField(max_length=100)),
                ('info_2', models.CharField(max_length=100)),
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Department')),
            ],
            options={
                'db_table': 'polls_department_info',
            },
        ),
    ]
