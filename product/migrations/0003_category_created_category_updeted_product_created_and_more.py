# Generated by Django 4.2.5 on 2023-09-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_description_category_img_alter_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updeted',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updeted',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
