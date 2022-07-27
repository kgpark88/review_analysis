# Generated by Django 4.0.6 on 2022-07-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField(blank=True, null=True, verbose_name='스토어 ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='작성자')),
                ('content', models.TextField(blank=True, null=True, verbose_name='내용')),
                ('source', models.CharField(blank=True, max_length=10, null=True, verbose_name='출처')),
                ('at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '리뷰',
                'verbose_name_plural': '리뷰',
                'db_table': 'review',
                'ordering': ['-at'],
                'managed': True,
            },
        ),
    ]
