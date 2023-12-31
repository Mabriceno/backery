# Generated by Django 3.2.22 on 2023-10-23 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_item_special_tax'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='base_price',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='enterprise',
            new_name='enterprise_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='category',
            new_name='item_category_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='bar_code',
            new_name='unit',
        ),
    ]
