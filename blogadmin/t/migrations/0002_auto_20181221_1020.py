# Generated by Django 2.1.4 on 2018-12-21 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('t', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='imgurl',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='artlist',
            new_name='artist',
        ),
    ]
