# Generated by Django 3.0.5 on 2020-05-12 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20200512_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='team_member',
            field=models.ManyToManyField(blank=True, related_name='teamMember_of', to=settings.AUTH_USER_MODEL),
        ),
    ]
