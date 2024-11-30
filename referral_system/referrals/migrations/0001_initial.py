# Generated by Django 4.2 on 2024-11-30 14:02

from django.db import migrations, models
import referrals.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('invite_code', models.CharField(default=referrals.models.generate_invite_code, max_length=6, unique=True)),
                ('activated_invite', models.CharField(blank=True, max_length=6, null=True)),
                ('invited_users', models.ManyToManyField(related_name='invited_by', to='referrals.user')),
            ],
        ),
    ]