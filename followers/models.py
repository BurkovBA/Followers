from django.db import models

# Create your models here.
class ManMan(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=32)
    follow_ids = models.TextField()

    class Meta:
        managed = True
        db_table = 'man_man'

