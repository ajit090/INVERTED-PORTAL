# Generated by Django 2.2 on 2022-07-21 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'APPLICATION',
            },
        ),
        migrations.AlterField(
            model_name='battery',
            name='battery_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.Application'),
        ),
    ]
