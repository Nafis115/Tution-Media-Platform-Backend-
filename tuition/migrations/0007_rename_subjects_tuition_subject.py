# Generated by Django 5.0.6 on 2024-09-26 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0006_alter_tuition_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tuition',
            old_name='subjects',
            new_name='subject',
        ),
    ]
