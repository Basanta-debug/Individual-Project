# Generated by Django 3.1.2 on 2021-04-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power', '0005_auto_20210407_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]