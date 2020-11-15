from __future__ import annotations

import json
import typing
from datetime import datetime

from rest_framework.response import Response

from api.models.users import User
from ..definitions import POST
from rest_framework.decorators import action
from api.models.inventory import Supply, Item, Upc, UpcList, UpcMap
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from ..utils import get_user_id_from_request


class InventoryViewSet(viewsets.ViewSet):

    @action(methods=[POST], detail=False)
    def get_supply(self, request: Request):

        user = get_user_id_from_request(request)
        if user:
            supply = Supply()
            inventory = supply.get_supply(user_id=user)
            return JsonResponse({"supply": list(inventory)})
        else:
            return HttpResponse(status=401)

    @action(methods=[POST], detail=False)
    def set_initial_inventory(self, request: Request):

        user = get_user_id_from_request(request)
        new_inventory = json.loads(request.data.get('inventory', None))
        if user and new_inventory:
            user = User(id=user)
            for item in new_inventory:
                item_id = Item.get_item_id(item.get('item', None))
                item_id = Item(id=item_id.id)
                inventory_item = Supply.objects.create(
                    user_id=user,
                    item_id=item_id,
                    amount=item.get('amount', 1),
                    date=datetime.now()
                )

            return Response(status=200)
        else:
            return HttpResponse(status=401)

    @action(methods=[POST], detail=False)
    def get_upc(self, request: Request):

        upc = Upc()
        upc_codes = upc.get_upc()
        return JsonResponse({"codes": list(upc_codes)})

    @action(methods=[POST], detail=False)
    def submit_upc(self, request: Request):
        user = get_user_id_from_request(request)
        code_list = json.loads(request.data.get('upc_list', None))
        if user and code_list:
            user = User(id=user)

            for code in code_list:
                upc_id = Upc.get_upc_id(code.get('upc', None))
                upc_id = Upc(id=upc_id.id)
                for i in range(1, int(code.get('amount', None)) + 1):
                    upc_list = UpcList(
                        user_id=user,
                        upc_id=upc_id,
                        date=datetime.now()
                    )
                    upc_list.save(force_insert=True)
            return Response(status=200)
        else:
            return HttpResponse(status=401)

    @action(methods=[POST], detail=False)
    def get_upc_list(self, request: Request):

        user = get_user_id_from_request(request)
        if user:
            upc_list = UpcList()
            upc_list = upc_list.get_upc_list(user_id=user)
            return JsonResponse({"upc_list": list(upc_list)})
        else:
            return HttpResponse(status=401)


if typing.TYPE_CHECKING:
    from rest_framework.request import Request