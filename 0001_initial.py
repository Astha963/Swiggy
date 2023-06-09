# Generated by Django 4.2 on 2023-05-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=20, null=True)),
                ('lastname', models.TextField(blank=True, max_length=20, null=True)),
                ('birth', models.DateField(blank=True, max_length=20, null=True)),
                ('mobile', models.IntegerField(blank=True, max_length=20, null=True)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=1)),
            ],
        ),
    ]
