# Generated by Django 4.0.5 on 2022-07-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_profile_pic_userinfo_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='facebook_id',
            field=models.URLField(blank=True),
        ),
    ]
