# Generated by Django 5.0.4 on 2024-04-24 11:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('ready', '미결제'), ('paid', '결제 완료'), ('cancelled', '결제 취소'), ('failed', '결제 실패')], db_index=True, default='ready', max_length=10)),
                ('is_paid', models.BooleanField(db_index=True, default=False)),
            ],
        ),
    ]
