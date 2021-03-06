# Generated by Django 3.2.11 on 2022-03-05 15:44

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220216_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=11, verbose_name='图片名')),
                ('picture', models.FileField(upload_to=app.models.rePath)),
            ],
        ),
    ]
