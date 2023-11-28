# Generated by Django 4.2.7 on 2023-11-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_schedule_created_alter_schedule_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_category',
            name='category',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Professional', 'Professional'), ('Entertainment', 'Entertainment'), ('Family', 'Family'), ('Friends', 'Friends')], default='personal', max_length=50),
        ),
    ]