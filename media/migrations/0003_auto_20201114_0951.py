# Generated by Django 3.1.3 on 2020-11-14 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20201114_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.CharField(max_length=20),
        ),
    ]
