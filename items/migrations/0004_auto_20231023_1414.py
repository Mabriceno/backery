# Generated by Django 3.2.22 on 2023-10-23 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20231023_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='enterprise_id',
            new_name='enterprise',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_category_id',
            new_name='item_category',
        ),
    ]
