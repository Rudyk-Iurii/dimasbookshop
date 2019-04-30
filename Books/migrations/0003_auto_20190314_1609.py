# Generated by Django 2.1.7 on 2019-03-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_auto_20190313_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='add_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='condition',
            field=models.CharField(default='Б/У', max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]