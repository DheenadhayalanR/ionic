# Generated by Django 4.1.1 on 2023-03-07 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_rename_post_postm'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postm',
            new_name='Details',
        ),
    ]
