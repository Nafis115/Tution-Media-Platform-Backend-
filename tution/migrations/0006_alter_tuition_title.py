# Generated by Django 5.0.6 on 2024-07-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0005_alter_subjectchoice_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuition',
            name='title',
            field=models.CharField(default='Tuition For', help_text='Title of the tuition', max_length=100),
        ),
    ]
