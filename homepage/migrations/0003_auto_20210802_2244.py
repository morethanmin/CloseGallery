# Generated by Django 3.2.5 on 2021-08-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_painting_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review_celebrity',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review_user',
            name='author',
        ),
        migrations.AddField(
            model_name='review_celebrity',
            name='thumbnail',
            field=models.CharField(default='', max_length=300, verbose_name='공간 사진'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review_user',
            name='thumbnail',
            field=models.CharField(default='', max_length=300, verbose_name='공간 사진'),
            preserve_default=False,
        ),
    ]
