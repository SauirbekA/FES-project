# Generated by Django 4.0 on 2023-01-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_learner_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner',
            name='photo',
            field=models.ImageField(blank=True, default='default/anonymous-user.png', null=True, upload_to='photos/users/'),
        ),
    ]
