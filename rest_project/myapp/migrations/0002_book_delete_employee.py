# Generated by Django 5.0 on 2024-01-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
