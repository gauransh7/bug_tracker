# Generated by Django 3.0.5 on 2020-05-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20200508_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='tag',
            field=models.ManyToManyField(null=True, related_name='tagIssues', to='tracker.Tag'),
        ),
    ]
