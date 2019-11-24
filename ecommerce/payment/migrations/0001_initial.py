# Generated by Django 2.2.7 on 2019-11-23 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone_no', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=120)),
                ('card_name', models.CharField(max_length=200, null=True)),
                ('card_number', models.CharField(max_length=18, null=True)),
                ('expiring_month', models.CharField(max_length=2, null=True)),
                ('expiring_year', models.CharField(max_length=2, null=True)),
                ('card_cvv', models.CharField(max_length=3, null=True)),
            ],
        ),
    ]
