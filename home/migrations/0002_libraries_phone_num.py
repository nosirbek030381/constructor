# Generated by Django 4.2.3 on 2023-07-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraries',
            name='phone_num',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
