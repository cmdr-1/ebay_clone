# Generated by Django 3.1.1 on 2020-10-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20201013_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='category',
            field=models.CharField(choices=[('Toys and Hobbies', 'Toys and Hobbies'), ('Auto', 'Auto'), ('Collectibles and Art', 'Collectibles and Art'), ('Fashion', 'Fashion'), ('Sporting Goods', 'Sporting Goods'), ('Electronics', 'Electronics'), ('Home and Garden', 'Home and Garden'), ('Other', 'Other')], default='other', max_length=64),
        ),
    ]