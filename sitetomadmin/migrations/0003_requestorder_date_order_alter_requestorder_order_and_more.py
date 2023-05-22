# Generated by Django 4.1.4 on 2023-02-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetomadmin', '0002_requestorder_classroom_requestorder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestorder',
            name='date_order',
            field=models.CharField(default='defaul', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requestorder',
            name='order',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='requestorder',
            name='person',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='requestorder',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
