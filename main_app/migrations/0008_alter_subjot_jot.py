# Generated by Django 3.2.7 on 2021-11-27 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20211125_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjot',
            name='jot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjots', to='main_app.jot'),
        ),
    ]