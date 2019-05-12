from django.db import models

# Create your models here.
class Item(models.Model):
    '''Эл-т списка'''
    text = models.TextField(default='')
