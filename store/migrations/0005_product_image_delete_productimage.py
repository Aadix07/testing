# Generated by Django 5.0.6 on 2024-07-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
