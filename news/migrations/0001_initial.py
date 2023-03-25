# Generated by Django 4.1.7 on 2023-03-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('title_uz', models.CharField(max_length=200, null=True)),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('text', models.TextField()),
                ('text_uz', models.TextField(null=True)),
                ('text_ru', models.TextField(null=True)),
            ],
        ),
    ]
