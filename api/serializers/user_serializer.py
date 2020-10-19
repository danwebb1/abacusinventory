from rest_framework import serializers
from abacusinventory.api.models.users import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['portal_key']
