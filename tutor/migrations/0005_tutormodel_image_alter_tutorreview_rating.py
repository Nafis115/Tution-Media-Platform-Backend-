# Generated by Django 5.0.6 on 2024-07-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0004_remove_tutormodel_preferred_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutormodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tutor/images/'),
        ),
        migrations.AlterField(
            model_name='tutorreview',
            name='rating',
            field=models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=10),
        ),
    ]
