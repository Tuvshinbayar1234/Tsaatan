# Generated by Django 3.1.7 on 2021-04-05 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210405_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='product-pictures')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
        ),
    ]
