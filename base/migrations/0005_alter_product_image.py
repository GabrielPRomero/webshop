# Generated by Django 3.2.8 on 2021-10-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/sampleImage.png', null=True, upload_to=''),
        ),
    ]
