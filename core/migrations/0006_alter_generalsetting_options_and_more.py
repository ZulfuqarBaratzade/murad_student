# Generated by Django 5.0.3 on 2024-05-16 10:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_imagesetting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalsetting',
            options={'ordering': ('name', 'paramater'), 'verbose_name': 'General Settings', 'verbose_name_plural': 'General Settings'},
        ),
        migrations.AlterModelOptions(
            name='imagesetting',
            options={'ordering': ('file',), 'verbose_name': 'Image Settings', 'verbose_name_plural': 'Image Settings'},
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Create Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
