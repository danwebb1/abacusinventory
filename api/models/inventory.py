from django.db import models
from .users import User


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=75)
    item_desc = models.CharField(max_length=240)
    item_code = models.CharField(max_length=50)

    class Meta:
        app_label = "Item"
        verbose_name = "Item"
        verbose_name_plural = "Items"
        db_table = 'item'

    @staticmethod
    def get_item_id(item):
        try:
            item_id = Item.objects.get(item_code=item)
        except ValueError:
            raise ValueError('No item found')

        return item_id if item_id else False


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

    @staticmethod
    def update_supply(user, upc_id):
        """
        Take the upc code and update the supply based on the UPC map values
        :param user: User
        :param upc_id: upc code id
        :return: None
        """
        update_supply = False
        _map = UpcMap.get_upc_map(user)
        code_list = []
        for code in _map:
            upc = Upc.get_upc_id(code.get('upc__upc', ''))
            if upc.id == upc_id:
                update_supply = True
                item = Item.get_item_id(code.get('item__item_code'))
                amount = code.get('amount', 0)
                old_amount = Supply.objects.get(user_id=user, item_id=item)
                new_amount = old_amount.amount - amount
                if new_amount >= 0:
                    to_update = Supply.objects.get(user_id=user, item_id=item)
                    to_update.amount = new_amount
                    to_update.save()
                else:
                    update = Supply.objects.filter(user_id=user, item_id=item).update(amount=0)

        if update_supply:
            return update
        else:
            return update_supply


class Upc(models.Model):
    id = models.AutoField(primary_key=True)
    upc = models.CharField(max_length=50)
    desc = models.CharField(max_length=155)

    class Meta:
        app_label = 'Upc'
        db_table = 'upc'

    @staticmethod
    def get_upc():
        """
        get the current upc codes
        :return: query set of upc
        """
        return Upc.objects.values('upc','desc')

    @staticmethod
    def get_upc_id(code):
        try:
            upc_id = Upc.objects.get(upc=code)
        except ValueError:
            raise ValueError('No item found')

        return upc_id if upc_id else False


class UpcList(models.Model):
    id = models.AutoField(primary_key=True)
    upc_id = models.ForeignKey(Upc, on_delete=models.CASCADE, db_column='upc_id')
    user_id = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE, db_column='user_id')
    date = models.DateTimeField()

    class Meta:
        managed = False
        app_label = 'UpcList'
        db_table = 'upc_list'

    @staticmethod
    def get_upc_list(user_id: User):
        """
        get the latest upc list for the given user
        :param user_id: User
        :return: query set of upc_list
        """
        upc_list = UpcList.objects.filter(user_id=user_id).order_by('-id')\
            .values('upc_id__upc',
                    'upc_id__desc',
                    'date')[:8]

        return upc_list


class UpcMap(models.Model):
    id = models.AutoField(primary_key=True)
    upc = models.ForeignKey(Upc, on_delete=models.CASCADE, db_column='upc')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, db_column='item')
    user_id = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE, db_column='user_id')
    amount = models.IntegerField(max_length=200)

    class Meta:
        app_label = 'ItemUpcMap'
        db_table = 'item_upc_map'

    @staticmethod
    def get_upc_map(user_id: User):
        """
        get the map list for the portal
        :param user_id: User
        :return: query set of upc_list
        """
        upc_map = UpcMap.objects.filter(user_id=user_id).order_by('id')\
            .values('upc__upc',
                    'upc__desc',
                    'item__item_code',
                    'item__item_name',
                    'amount')

        return upc_map
