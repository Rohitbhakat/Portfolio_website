# Generated by Django 3.0.8 on 2020-11-10 18:25

from django.db import migrations
import smartfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_content', '0013_seo_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail_img',
            field=smartfields.fields.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]