# Generated by Django 4.0 on 2024-02-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner',
            name='phone',
            field=models.TextField(default=87798743),
            preserve_default=False,
        ),
    ]