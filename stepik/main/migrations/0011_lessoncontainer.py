# Generated by Django 4.0 on 2023-01-21 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_video_content_alter_video_idcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUser', models.IntegerField()),
                ('idCourse', models.IntegerField()),
            ],
        ),
    ]