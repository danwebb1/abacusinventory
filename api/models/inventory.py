from django.db import models
from .users import User


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=75)
    item_description = models.CharField(max_length=240)
    item_code = models.CharField(max_length=50)

    class Meta:
        app_label = "Item"
        verbose_name = "Item"
        verbose_name_plural = "Items"
        db_table = 'item'


class Supply(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    item_id = models.ForeignKey(Item, related_name="items", on_delete=models.CASCADE, db_column='item_id')
    amount = models.IntegerField(max_length=200)
    date = models.DateTimeField()

    class Meta:
        app_label = 'Supply'
        db_table = 'supply'

    @staticmethod
    def get_supply(user_id: User):
        """
        get the current inventory supply for the given user
        :param user_id: User
        :return: query set of supply
        """
        inventory = Supply.objects.filter(user_id=user_id).order_by('id')\
            .values('amount',
                    'date',
                    'item_id__item_name',
                    'item_id__item_code')

        return inventory


class Upc(models.Model):
    id = models.AutoField(primary_key=True)
    upc = models.CharField(max_length=50)

    class Meta:
        app_label = 'Upc'
        db_table = 'upc'


class UpcList(models.Model):
    id = models.AutoField(primary_key=True)
    upc_id = models.ForeignKey(Upc, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'UpcList'
        db_table = 'upc_list'


class UpcMap(models.Model):
    upc = models.ForeignKey(Upc, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        app_label = 'UpcMap'
        db_table = 'upc_map'
