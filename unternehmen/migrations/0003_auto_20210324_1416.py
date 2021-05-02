# Generated by Django 3.1.7 on 2021-03-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unternehmen', '0002_auto_20210324_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='average_words',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='tweets_after_10_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='tweets_after_20_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='tweets_after_30_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='unternehmena',
            name='datum',
            field=models.DateField(default='--', max_length=20),
        ),
    ]