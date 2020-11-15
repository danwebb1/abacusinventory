from rest_framework import serializers
from ..models.inventory import Supply, Item, UpcMap, UpcList, Upc


class SupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
        fields = ['user_id', 'item_id', 'amount', 'date']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'item_description']


class UpcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upc
        fields = ['upc']


class UpcMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcMap
        fields = ['upc', 'item']


class UpcListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcList
        fields = ['user_id', 'upc_id', 'date']
