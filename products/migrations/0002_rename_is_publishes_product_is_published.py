# Generated by Django 4.1.2 on 2022-10-09 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_publishes',
            new_name='is_published',
        ),
    ]
