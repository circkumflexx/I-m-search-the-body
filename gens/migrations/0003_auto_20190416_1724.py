# Generated by Django 2.2 on 2019-04-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gens', '0002_auto_20190414_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadbody',
            name='items_string',
            field=models.TextField(),
        ),
    ]
