# Generated by Django 3.2.8 on 2021-10-14 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=200)),
                ('videoId', models.CharField(max_length=50)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=200)),
                ('commentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
            ],
        ),
    ]
