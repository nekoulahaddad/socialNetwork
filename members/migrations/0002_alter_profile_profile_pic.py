# Generated by Django 3.2.4 on 2021-06-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='img/user/default.jpg', null=True, upload_to='img/user/'),
        ),
    ]