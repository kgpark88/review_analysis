# Generated by Django 4.0.6 on 2022-07-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_review_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='작성일'),
        ),
        migrations.AlterField(
            model_name='review',
            name='source',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='구분'),
        ),
    ]
