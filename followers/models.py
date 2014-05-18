from django.db import models

# Create your models here.
class Man(models.Model):
#    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=32)
    follow_ids = models.TextField()

    class Meta:
        managed = True
        db_table = 'man_man'

    def __str__(self):
        return "%s, id=%s" % (self.name, self.id)

class Follow(models.Model):
    who = models.ForeignKey('Man', related_name='who')
    whom = models.ForeignKey('Man', related_name='whom')
