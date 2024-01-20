# Generated by Django 5.0.1 on 2024-01-20 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_giftcard_giftcardcompany_order_trashsubmission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftcard',
            name='giftCardNumber',
        ),
        migrations.AlterField(
            model_name='giftcard',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.giftcardcompany'),
        ),
    ]
