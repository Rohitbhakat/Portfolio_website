# Generated by Django 3.0.8 on 2020-11-12 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_content', '0018_head_footer_gif_404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='head_footer',
            name='gif_404',
        ),
    ]
