# Generated by Django 3.1.2 on 2021-04-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power', '0006_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vacancyform',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]