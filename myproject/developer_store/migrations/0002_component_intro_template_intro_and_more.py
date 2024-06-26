# Generated by Django 5.0.6 on 2024-06-05 14:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='intro',
            field=models.CharField(default=django.utils.timezone.now, help_text='Short introduction for component, shown on the card.', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='intro',
            field=models.CharField(default=django.utils.timezone.now, help_text='Short introduction for template, shown on the card.', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='component',
            name='description',
            field=models.TextField(help_text='Full description that can include HTML, shown in modal.'),
        ),
        migrations.AlterField(
            model_name='template',
            name='description',
            field=models.TextField(help_text='Full description that can include HTML, shown in modal.'),
        ),
    ]
