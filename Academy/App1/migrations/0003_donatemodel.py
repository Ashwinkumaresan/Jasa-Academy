# Generated by Django 5.1.1 on 2024-09-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_rename_compition_formmodel_competition'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=26)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
