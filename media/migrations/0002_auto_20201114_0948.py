# Generated by Django 3.1.3 on 2020-11-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='title',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.TextField(),
        ),
    ]
