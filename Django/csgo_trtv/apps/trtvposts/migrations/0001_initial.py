# Generated by Django 4.2.4 on 2023-08-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='posts/covers/%Y/%m/%d')),
                ('video', models.URLField(blank=None, null=None)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('highlight', 'Highlight'), ('strategy', 'Strategy'), ('basics', 'Academy')], max_length=12)),
                ('slug', models.SlugField(blank=None, null=None, unique=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
