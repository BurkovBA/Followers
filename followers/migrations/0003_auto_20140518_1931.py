# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0002_follows'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follows',
            new_name='Follow',
        ),
    ]
