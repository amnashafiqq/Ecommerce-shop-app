# Generated by Django 4.2.3 on 2023-08-04 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
