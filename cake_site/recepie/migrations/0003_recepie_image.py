# Generated by Django 3.2 on 2021-04-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepie', '0002_recepie_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepie',
            name='image',
            field=models.ImageField(default='no-image.png', upload_to='recepie', verbose_name='image'),
        ),
    ]
