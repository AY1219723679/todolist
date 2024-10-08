# Generated by Django 5.1 on 2024-08-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=250)),
                ('is_complete', models.BooleanField(default=False)),
                ('create_at', models.TimeField(auto_now_add=True)),
                ('modify_at', models.TimeField(auto_now=True)),
            ],
        ),
    ]
