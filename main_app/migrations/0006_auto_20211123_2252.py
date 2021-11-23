# Generated by Django 3.2.7 on 2021-11-23 22:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_subjot_jot'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubJot',
            new_name='SubTask',
        ),
        migrations.RenameModel(
            old_name='Jot',
            new_name='Task',
        ),
        migrations.RenameField(
            model_name='subtask',
            old_name='jot',
            new_name='task',
        ),
    ]
