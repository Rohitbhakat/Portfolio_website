# Generated by Django 3.0.8 on 2020-11-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_content', '0017_head_footer_video_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='head_footer',
            name='gif_404',
            field=models.FileField(null=True, upload_to='pics'),
        ),
    ]