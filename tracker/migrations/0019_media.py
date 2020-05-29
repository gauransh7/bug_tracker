# Generated by Django 3.0.5 on 2020-05-27 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0018_auto_20200519_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ImageField(upload_to='upload_images')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_media', to='tracker.Project')),
            ],
        ),
    ]