# Generated by Django 5.0.6 on 2024-09-26 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0007_rename_subjects_tuition_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tuition',
            old_name='subject',
            new_name='subjects',
        ),
    ]
