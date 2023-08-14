# Generated by Django 4.2.4 on 2023-08-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trtvposts', '0002_post_map_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('pt', 'Portuguese'), ('ru', 'Russian'), ('sp', 'Spanish')], default='en', max_length=24),
        ),
    ]
