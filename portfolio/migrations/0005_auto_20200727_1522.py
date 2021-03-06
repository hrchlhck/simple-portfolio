# Generated by Django 3.0.8 on 2020-07-27 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200714_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(error_messages={'unique': 'The name of the project is not unique. Please try again.'}, help_text='must be a unique name', max_length=30, unique=True),
        ),
    ]
