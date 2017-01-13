from django.db import models


# Create your models here.

class ParserCsv(models.Model):
    upload = models.FileField(blank=True)


class CsvList(models.Model):
    id = models.AutoField
    first_name = models.CharField(blank=True, max_length=200)
    last_name = models.CharField(blank=True, max_length=200)
    email = models.EmailField(blank=True)
    domain = models.TextField(blank=True)
    url = models.URLField(blank=True, null=True)
