# Generated by Django 3.1.7 on 2021-03-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unternehmen', '0003_auto_20210324_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unternehmensname', models.CharField(default='--', max_length=100)),
                ('userId', models.CharField(default='--', max_length=100)),
                ('datum', models.DateField(default='--', max_length=20)),
                ('tweet', models.TextField(default='--', max_length=280)),
                ('zeichen', models.IntegerField(default=0)),
                ('woerter', models.IntegerField(default=0)),
                ('schluesselId', models.CharField(default='', editable=False, max_length=100)),
            ],
            options={
                'verbose_name': 'Tweet',
                'verbose_name_plural': 'Tweets',
            },
        ),
        migrations.DeleteModel(
            name='unternehmena',
        ),
    ]