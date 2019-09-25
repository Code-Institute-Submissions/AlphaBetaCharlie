# Python bytecode 3.7 (3394)
# Embedded file name: /workspace/AlphaBetaCharlie/products/migrations/0002_auto_20190924_1435.py
# Size of source mod 2**32: 3855 bytes
# Decompiled by https://python-decompiler.com
from __future__ import unicode_literals
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc

class Migration(migrations.Migration):
    dependencies = [
     migrations.swappable_dependency(settings.AUTH_USER_MODEL),
     ('products', '0001_initial')]
    operations = [
     migrations.CreateModel(name='ProductBase',
       fields=[
      (
       'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'name', models.CharField(max_length=200))]),
     migrations.CreateModel(name='ProductType',
       fields=[
      (
       'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'name', models.CharField(max_length=200)),
      (
       'description', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
      (
       'price', models.DecimalField(decimal_places=2, max_digits=6)),
      (
       'image_available', models.ImageField(blank=True, upload_to='images')),
      (
       'image_consumed', models.ImageField(blank=True, upload_to='images')),
      (
       'created_at', models.DateTimeField(auto_now_add=True)),
      (
       'updated_at', models.DateTimeField(auto_now=True)),
      (
       'base', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.DO_NOTHING), to='products.ProductBase'))]),
     migrations.RemoveField(model_name='product',
       name='description'),
     migrations.RemoveField(model_name='product',
       name='image'),
     migrations.RemoveField(model_name='product',
       name='name'),
     migrations.RemoveField(model_name='product',
       name='price'),
     migrations.AddField(model_name='product',
       name='consumed_by',
       field=models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.DO_NOTHING), related_name='user_consumed_by', to=(settings.AUTH_USER_MODEL))),
     migrations.AddField(model_name='product',
       name='created_at',
       field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 9, 24, 14, 35, 59, 106072, tzinfo=utc)),
       preserve_default=False),
     migrations.AddField(model_name='product',
       name='created_by',
       field=models.ForeignKey(null=True, on_delete=(django.db.models.deletion.DO_NOTHING), related_name='user_created_by', to=(settings.AUTH_USER_MODEL))),
     migrations.AddField(model_name='product',
       name='parent',
       field=models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.DO_NOTHING), related_name='product', to='products.Product')),
     migrations.AddField(model_name='product',
       name='status',
       field=models.CharField(blank=True, choices=[('available', 'Available'), ('held', 'Held'), ('consumed', 'Consumed')], default='available', help_text='Product Status', max_length=15)),
     migrations.AddField(model_name='product',
       name='updated_at',
       field=models.DateTimeField(auto_now=True)),
     migrations.AddField(model_name='product',
       name='type',
       field=models.ForeignKey(null=True, on_delete=(django.db.models.deletion.DO_NOTHING), to='products.ProductType'))]