# Generated by Django 3.2.11 on 2022-02-14 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220211_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('headimg', models.FileField(upload_to='file')),
            ],
        ),
        migrations.DeleteModel(
            name='UserVideo',
        ),
    ]