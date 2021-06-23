# Generated by Django 3.2.3 on 2021-06-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
