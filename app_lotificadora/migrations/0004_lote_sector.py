# Generated by Django 3.2.5 on 2021-07-28 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_lotificadora', '0003_auto_20210728_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_lotificadora.sector'),
        ),
    ]