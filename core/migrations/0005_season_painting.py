# Generated by Django 3.2.5 on 2021-08-03 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210802_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season_painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.painting')),
            ],
        ),
    ]