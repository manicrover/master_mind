# Generated by Django 4.0.3 on 2022-03-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='age_limit',
            field=models.CharField(default='none', max_length=500),
        ),
    ]
