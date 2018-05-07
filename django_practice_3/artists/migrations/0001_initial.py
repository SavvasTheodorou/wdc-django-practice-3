# Generated by Django 2.0 on 2018-05-06 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('artistic_name', models.CharField(max_length=255)),
                ('picture_url', models.URLField()),
                ('popularity', models.IntegerField()),
                ('genre', models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('album_name', models.CharField(max_length=255)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Artist')),
            ],
        ),
    ]
