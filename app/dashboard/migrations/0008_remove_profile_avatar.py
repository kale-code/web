# Generated by Django 2.1.4 on 2019-01-14 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20190118_1832'),
    ]

    operations = [
        migrations.RunSQL("create table dashboard_profile_tmp as select * from dashboard_profile;"),
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]
