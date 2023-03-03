# Generated by Django 4.1.5 on 2023-02-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proj1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('is_staff', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]
