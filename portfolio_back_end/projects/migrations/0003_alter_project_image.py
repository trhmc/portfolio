# Generated by Django 4.2.1 on 2023-05-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='projects/img/'),
        ),
    ]
