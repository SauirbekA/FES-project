# Generated by Django 4.0 on 2023-03-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_video_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUser', models.IntegerField()),
                ('idCourse', models.IntegerField()),
            ],
        ),
    ]