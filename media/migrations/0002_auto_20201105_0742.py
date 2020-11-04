# Generated by Django 3.1.3 on 2020-11-04 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contents',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='contents',
            name='id',
        ),
        migrations.AddField(
            model_name='contents',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contents',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='image/posts/'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contents',
            name='post_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
