# Generated by Django 4.2.3 on 2023-08-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_item_category_item_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test-product'),
            preserve_default=False,
        ),
    ]
