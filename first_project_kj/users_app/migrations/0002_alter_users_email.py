# Generated by Django 3.2.5 on 2021-07-24 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
