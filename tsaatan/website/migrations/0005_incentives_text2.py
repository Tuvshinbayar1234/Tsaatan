# Generated by Django 3.1.7 on 2021-03-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_incentives'),
    ]

    operations = [
        migrations.AddField(
            model_name='incentives',
            name='text2',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
