# Generated by Django 3.2.5 on 2021-07-31 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_lotificadora', '0006_auto_20210730_0339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sector',
            old_name='Cantidad',
            new_name='cantidad',
        ),
    ]