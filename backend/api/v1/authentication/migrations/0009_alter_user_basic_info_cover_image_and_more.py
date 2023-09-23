# Generated by Django 4.2.1 on 2023-09-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_user_basic_info_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_basic_info',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_image'),
        ),
        migrations.AlterField(
            model_name='user_basic_info',
            name='your_photo',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='user_image'),
        ),
    ]