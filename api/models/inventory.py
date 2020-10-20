from django.db import models
from .users import User


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=75)
    item_description = models.CharField(max_length=240)

    class Meta:
        app_label = "Item"
        verbose_name = "Item"
        verbose_name_plural = "Items"


class Supply(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField(max_length=200)
    date = models.DateField()

    class Meta:
        app_label = "Supply"


class Upc(models.Model):
    id = models.AutoField(primary_key=True)
    upc = models.CharField(max_length=50)

    class Meta:
        app_label = "Upc"


class UpcList(models.Model):
    id = models.AutoField(primary_key=True)
    upc_id = models.ForeignKey(Upc, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = "UpcList"


class UpcMap(models.Model):
    upc = models.ForeignKey(Upc, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        app_label = "UpcMap"
