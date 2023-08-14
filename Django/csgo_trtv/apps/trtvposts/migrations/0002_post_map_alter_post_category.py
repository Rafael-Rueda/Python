# Generated by Django 4.2.4 on 2023-08-03 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trtvposts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='map',
            field=models.CharField(choices=[('de_ancient', 'Ancient'), ('de_anubis', 'Anubis'), ('de_cache', 'Cache'), ('de_dust2', 'Dust 2'), ('de_inferno', 'Inferno'), ('de_mirage', 'Mirage'), ('de_nuke', 'Nuke'), ('de_overpass', 'Overpass'), ('de_train', 'Train'), ('de_tuscan', 'Tuscan'), ('de_vertigo', 'Vertigo'), ('cs_agency', 'Agency (CS)'), ('cs_office', 'Office (CS)')], default='de_ancient', max_length=16),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('highlight', 'Highlight'), ('strategy', 'Strategy'), ('basics', 'Academy'), ('solo', 'Solo Play')], default='highlight', max_length=12),
        ),
    ]
