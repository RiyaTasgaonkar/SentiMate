# Generated by Django 3.1.7 on 2021-04-05 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('SentiMate', '0006_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestB',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('o', models.IntegerField()),
                ('c', models.IntegerField()),
                ('e', models.IntegerField()),
                ('a', models.IntegerField()),
                ('n', models.IntegerField()),
            ],
        ),
    ]
