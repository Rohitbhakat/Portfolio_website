# Generated by Django 3.0.8 on 2020-11-09 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_content', '0004_auto_20201109_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_detail',
            name='subject',
        ),
    ]
