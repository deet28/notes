# Generated by Django 4.1 on 2022-08-23 13:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_alter_notebook_topic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NoteBook',
            new_name='Book',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='notebook',
            new_name='book',
        ),
    ]
