# Generated by Django 5.1 on 2024-12-03 09:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_remove_all_posts_follow_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='foll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
