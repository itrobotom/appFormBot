# Generated by Django 4.1.4 on 2023-02-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetomadmin', '0004_requestorder_computer'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestorder',
            name='family_user_tg',
            field=models.CharField(default='11', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestorder',
            name='id_user',
            field=models.CharField(default='11', max_length=30),
            preserve_default=False,
        ),
    ]
