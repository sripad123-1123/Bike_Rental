# Generated by Django 3.2.3 on 2021-06-08 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210606_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='total_time',
            field=models.IntegerField(null='True'),
            preserve_default='True',
        ),
    ]