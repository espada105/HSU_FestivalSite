# Generated by Django 3.2.20 on 2023-09-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbs_up', '0005_intruduce_imagecheack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intruduce',
            name='imagecheack',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
