# Generated by Django 5.0.6 on 2024-09-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_rename_subjects_tutormodel_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutormodel',
            name='subject',
        ),
        migrations.AddField(
            model_name='tutormodel',
            name='subjects',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='SubjectChoice',
        ),
    ]
