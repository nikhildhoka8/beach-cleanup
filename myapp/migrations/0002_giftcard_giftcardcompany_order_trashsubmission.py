# Generated by Django 5.0.1 on 2024-01-20 16:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giftCardNumber', models.IntegerField(unique=True)),
                ('company', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GiftCardCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateField(auto_now_add=True)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('giftCardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.giftcard')),
            ],
        ),
        migrations.CreateModel(
            name='TrashSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='trash_images/')),
                ('mapsURL', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('validity', models.BooleanField(default=False)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
