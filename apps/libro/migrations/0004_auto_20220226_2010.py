# Generated by Django 3.2 on 2022-02-27 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_rename_autor_id_libro_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.autor'),
        ),
    ]
