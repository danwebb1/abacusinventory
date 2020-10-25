from rest_framework import serializers
from ..models.inventory import Supply, Item, UpcMap, UpcList, Upc


class SupplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Supply
        fields = ['user_id', 'item_id', 'amount', 'date']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ['item_name', 'item_description']


class UpcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ['upc']


class UpcMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ['upc', 'item']


class UpcListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ['upc_id', 'item_id', 'user_id']
