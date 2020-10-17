# Generated by Django 3.1.1 on 2020-10-16 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20201015_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='listing',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listing',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='watched_listings', to='auctions.listings'),
            preserve_default=False,
        ),
    ]
