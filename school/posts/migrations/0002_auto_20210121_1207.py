# Generated by Django 3.1.3 on 2021-01-21 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='follow',
            name='author',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
