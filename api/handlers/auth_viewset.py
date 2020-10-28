from __future__ import annotations

import datetime
import typing

from api.models.inventory import Supply, Item
from api.utils import get_user_id_from_request
from ..definitions import GET, POST
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models.users import User
from rest_framework import viewsets
from django.http import HttpResponse


class AuthViewSet(viewsets.ViewSet):

    @action(methods=[POST], detail=False)
    def create_portal(self, request: Request):

        portal = request.data.get('portal', None)
        if portal:
            new_user = User(portal_firestore_key=portal)
            new_user.save()
            return Response(status=200)
        else:
            return HttpResponse(status=401)

    @action(methods=[POST], detail=False)
    def create_inventory(self, request: Request):

        user = get_user_id_from_request(request)
        if user:
            item = Item(id=0)
            user = User(id=user)
            new_inventory = Supply(user_id=user, item_id=item, amount=0, date=datetime.datetime.now())
            new_inventory.save()
            return Response(status=200)
        else:
            return HttpResponse(status=401)


if typing.TYPE_CHECKING:
    from rest_framework.request import Request