# Generated by Django 2.2.4 on 2019-08-09 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190809_1944'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileFeed',
            new_name='ProfileFeedItem',
        ),
    ]
