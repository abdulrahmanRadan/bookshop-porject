# Generated by Django 5.0.6 on 2024-06-19 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('city1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city1_roads', to='books.city')),
                ('city2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city2_roads', to='books.city')),
            ],
            options={
                'unique_together': {('city1', 'city2')},
            },
        ),
    ]