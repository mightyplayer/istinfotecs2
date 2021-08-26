from django.db import models


class Product(models.Model):
    infotecs_id = models.CharField(None, max_length=200)
    name = models.CharField(None, max_length=200)
    description = models.TextField(None)
    is_parent = models.BooleanField(None)
    parent_ID = models.CharField(None, max_length=200)
    price_modifier = models.FloatField(None)
    price_dict = models.JSONField()


