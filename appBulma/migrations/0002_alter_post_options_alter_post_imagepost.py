# Generated by Django 4.1.7 on 2023-02-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBulma', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='imagePost',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Image'),
        ),
    ]
