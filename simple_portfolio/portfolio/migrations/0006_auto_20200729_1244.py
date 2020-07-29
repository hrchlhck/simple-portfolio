# Generated by Django 3.0.8 on 2020-07-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200727_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='project',
            name='updated',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(upload_to='project_images', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
    ]
