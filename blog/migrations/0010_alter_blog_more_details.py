# Generated by Django 4.0.3 on 2022-03-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blog_cut_off_alter_blog_more_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='more_details',
            field=models.CharField(max_length=1000),
        ),
    ]
