# Generated by Django 3.1.3 on 2020-11-15 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_auto_20201114_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
