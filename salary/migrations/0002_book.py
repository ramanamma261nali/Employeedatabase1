# Generated by Django 4.2.4 on 2023-08-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=100)),
                ('Author_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images')),
            ],
        ),
    ]
