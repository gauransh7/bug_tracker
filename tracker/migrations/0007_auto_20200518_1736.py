# Generated by Django 3.0.5 on 2020-05-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20200512_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
