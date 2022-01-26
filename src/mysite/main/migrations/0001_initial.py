# Generated by Django 3.2.8 on 2021-10-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=256)),
                ('work', models.CharField(max_length=256)),
            ],
        ),
    ]
