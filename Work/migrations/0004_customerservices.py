# Generated by Django 4.1 on 2022-08-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('details', models.TextField(max_length=500)),
            ],
        ),
    ]
