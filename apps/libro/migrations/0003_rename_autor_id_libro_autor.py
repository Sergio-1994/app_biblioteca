# Generated by Django 3.2 on 2022-02-27 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20220210_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='autor_id',
            new_name='autor',
        ),
    ]
