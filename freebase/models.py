from django.db import models

class Model(models.model):
    name = models.CharField(max_length=30)
    fields = models.ManyToManyField(Field)

class Field(models.model):
    TYPES = (
        ('CHAR',     'Simple Text'),
        ('DATETIME', 'Date/Time'),
        ('INT',      'Number'),
        ('TXT',      'Large Textarea'),
    )
    name = models.CharField(max_length=30)
    data_type = models.CharField(choices=TYPES)