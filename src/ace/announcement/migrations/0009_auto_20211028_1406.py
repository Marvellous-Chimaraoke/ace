# Generated by Django 3.2.6 on 2021-10-28 13:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('announcement', '0008_auto_20211028_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 13, 6, 32, 2245, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
