# Generated by Django 3.2.5 on 2021-07-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lotificadora', '0005_auto_20210730_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lote',
            old_name='vendido',
            new_name='estado',
        ),
        migrations.RemoveField(
            model_name='lote',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='sector',
            name='ubicacion',
            field=models.CharField(max_length=40, null=True),
        ),
    ]