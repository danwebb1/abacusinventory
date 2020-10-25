from rest_framework import serializers
from api.models.users import User


class UserSerializer(serializers.ModelSerializer):
    def update(self, instance: User, validated_data: dict) -> User:
        """
        Update a bulk quote entity
        :param instance: BulkQuoteSearch to update
        :param validated_data: Data to update with
        :return: Updated Entity
        """
        instance.save()
        return instance

    def create(self, validated_data: dict) -> User:
        """
        Create a new bulk quote entity
        :param validated_data: data to create with
        :return: Created Entity
        """
        instance = User(**validated_data)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['portal_firestore_key']
