# Generated by Django 3.2.22 on 2023-10-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=12)),
                ('giro', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]