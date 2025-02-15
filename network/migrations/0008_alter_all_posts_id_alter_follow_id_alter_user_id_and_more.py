# Generated by Django 5.1 on 2024-12-06 08:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_alter_follow_foll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_posts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.all_posts')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liking', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
