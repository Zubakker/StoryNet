# Generated by Django 3.2.5 on 2021-08-06 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_myuser_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]