# Generated by Django 4.2.16 on 2024-09-22 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_alter_comment_approver_note_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ing_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ING_ID')),
                ('ing_name', models.CharField()),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('unit', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_id',
            new_name='recipe',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/'),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=50)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(through='recipe.RecipeIngredient', to='recipe.ingredient'),
        ),
    ]
