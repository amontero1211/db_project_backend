# Generated by Django 4.1.1 on 2022-10-02 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_artwork_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaser',
            name='card_expiration_date',
        ),
        migrations.RemoveField(
            model_name='purchaser',
            name='purchase_key',
        ),
    ]
