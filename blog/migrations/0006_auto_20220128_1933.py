# Generated by Django 3.2.7 on 2022-01-28 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220128_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='gönderi',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='baslik',
            new_name='title',
        ),
    ]