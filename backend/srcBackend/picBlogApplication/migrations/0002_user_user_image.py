# Generated by Django 3.1.3 on 2020-11-29 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picBlogApplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, upload_to='static/PicBlogApplication/images/'),
        ),
    ]
