# Generated by Django 3.2.5 on 2021-08-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='biograpy',
            new_name='biography',
        ),
        migrations.AddField(
            model_name='myuser',
            name='full_name',
            field=models.CharField(default='пётр лапа', max_length=256),
            preserve_default=False,
        ),
    ]
