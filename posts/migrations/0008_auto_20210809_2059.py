# Generated by Django 3.2.5 on 2021-08-09 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210809_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='epigraph_author',
            new_name='epigr_author',
        ),
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='posts.Genre'),
        ),
    ]
