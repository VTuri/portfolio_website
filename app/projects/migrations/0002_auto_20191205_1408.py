# Generated by Django 2.2.7 on 2019-12-05 14:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
