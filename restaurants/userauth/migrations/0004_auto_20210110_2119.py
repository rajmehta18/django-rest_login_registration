# Generated by Django 3.1.5 on 2021-01-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_auto_20210110_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
