# Generated by Django 2.2.5 on 2019-09-24 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.ProductType'),
        ),
    ]
