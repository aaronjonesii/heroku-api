# Generated by Django 2.1.4 on 2019-01-15 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('imdb_id', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=4)),
                ('slug', models.CharField(max_length=150)),
                ('synopsis', models.TextField()),
                ('runtime', models.CharField(max_length=4)),
                ('country', models.CharField(max_length=4)),
                ('last_updated', models.FloatField(max_length=16)),
                ('released', models.IntegerField()),
                ('certification', models.CharField(max_length=255)),
                ('torrents', models.TextField()),
                ('trailer', models.CharField(max_length=255)),
                ('genres', models.CharField(max_length=255)),
                ('images', models.TextField()),
                ('rating', models.CharField(max_length=255)),
                ('_v', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]