# Generated by Django 2.0.3 on 2018-03-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_bounties', '0002_externalbounty_payout_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalbounty',
            name='amount',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='externalbounty',
            name='amount_denomination',
            field=models.CharField(blank=True, help_text='ex: ETH, LTC, BTC', max_length=255),
        ),
        migrations.AlterField(
            model_name='externalbounty',
            name='payout_str',
            field=models.CharField(default='', help_text='string representation of the payout (only needed it amount/denomination cannot be filled out', max_length=255),
        ),
    ]
