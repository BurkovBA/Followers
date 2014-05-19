# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0003_auto_20140518_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='man',
            name='follow_ids',
        ),
    ]
