# Generated by Django 4.2.16 on 2024-09-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_alter_recipe_cook_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approver_note',
            field=models.CharField(default=None),
        ),
    ]
