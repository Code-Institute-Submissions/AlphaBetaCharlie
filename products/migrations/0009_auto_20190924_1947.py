# Generated by Django 2.2.5 on 2019-09-24 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190924_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.ProductType'),
        ),
    ]
