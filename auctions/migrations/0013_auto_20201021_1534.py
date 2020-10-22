# Generated by Django 3.1.1 on 2020-10-21 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_listings_current_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='active',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='listings',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
    ]
