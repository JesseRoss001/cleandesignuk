# Generated by Django 5.0.6 on 2024-08-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_content_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Meta description for SEO (max 160 characters)', max_length=160),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_keywords',
            field=models.CharField(blank=True, help_text='Comma-separated keywords for SEO', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Title for SEO (max 70 characters)', max_length=70),
        ),
    ]
