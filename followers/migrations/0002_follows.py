# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follows',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('who', models.ForeignKey(to='followers.Man', to_field=u'id')),
                ('whom', models.ForeignKey(to='followers.Man', to_field=u'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
