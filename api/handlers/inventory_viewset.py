from __future__ import annotations

import json
import typing
from datetime import datetime

from rest_framework.response import Response

from api.models.users import User
from ..definitions import POST, PUT
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
                if Supply.objects.filter(user_id=user, item_id=item_id):
                    old_amount = Supply.objects.get(user_id=user, item_id=item_id)
                    new_amount = old_amount.amount + int(item.get('amount', 0))
                    to_update = Supply.objects.get(user_id=user, item_id=item_id)
                    to_update.amount = new_amount
                    to_update.save()
                else:
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
                    supply = Supply()
                    update_supply = supply.update_supply(user=user, upc_id=upc_id.id)
                    if not update_supply:
                        raise ValueError('The submitted UPC has not been mapped for this practice.')
                    upc_list.save(force_insert=True)
            return Response(status=200)
        else:
            return HttpResponse(status=401)

    @action(methods=[POST], detail=False)
    def submit_upc_map(self, request: Request):
        user = get_user_id_from_request(request)
        map_list = json.loads(request.data.get('map_list', None))
        if user and map_list:
            user = User(id=user)
            for code in map_list:
                for list_item in code:
                    upc_id = Upc.get_upc_id(list_item.get('upc', None))
                    upc_id = Upc(id=upc_id.id)
                    item_id = Item.get_item_id(list_item.get('item', None))
                    item_id = Item(id=item_id.id)
                    upc_list = UpcMap(
                        user_id=user,
                        upc=upc_id,
                        item=item_id,
                        amount=list_item.get('amount', 0)
                    )
                    upc_list.save(force_insert=True)
            return Response(status=200)
        else:
            return HttpResponse(status=401)

    @action(methods=[PUT], detail=False)
    def update_upc_map(self, request: Request):
        user = get_user_id_from_request(request)
        map_list = json.loads(request.data.get('map_list', None))
        if user and map_list:
            user = User(id=user)
            for code in map_list.get('upc_map', {}):
                upc_id = Upc.get_upc_id(code.get('upc__upc', None))
                item_id = Item.get_item_id(code.get('item__item_code', None))
                if UpcMap.objects.filter(upc=upc_id, user_id=user, item=item_id):
                    to_update = UpcMap.objects.get(upc=upc_id, user_id=user, item=item_id)
                    to_update.amount = code.get('amount')
                    to_update.save()
                elif not UpcMap.objects.filter(upc=upc_id, user_id=user, item=item_id):
                    upc_list = UpcMap(
                        user_id=user,
                        upc=upc_id,
                        item=item_id,
                        amount=code.get('amount', 0)
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

    @action(methods=[POST], detail=False)
    def get_upc_map(self, request: Request):
        user = get_user_id_from_request(request)
        if user:
            upc_mappings = UpcMap()
            upc_map = upc_mappings.get_upc_map(user_id=user)
            return JsonResponse({"upc_map": list(upc_map)})
        else:
            return HttpResponse(status=401)


if typing.TYPE_CHECKING:
    from rest_framework.request import Request