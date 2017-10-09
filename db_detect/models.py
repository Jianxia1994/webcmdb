from django.db import models

# Create your models here.


class Db_info(models.Model):
    ip = models.CharField(max_length=200)
    dbs = models.CharField(max_length=500)
    def __str__(self):
        return self.ip
