# Generated by Django 4.1.1 on 2022-09-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_artist_purchaser_artwork_create_date_artwork_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaser',
            name='answer_1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='purchaser',
            name='answer_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='purchaser',
            name='answer_3',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='purchaser',
            name='purchase_key',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='purchaser',
            name='question_1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='purchaser',
            name='question_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='purchaser',
            name='question_3',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='state',
            field=models.CharField(choices=[('available', 'Disponible'), ('reserved', 'Reservado'), ('sold_out', 'Vendido')], default='available', max_length=10),
        ),
    ]
