from __future__ import annotations

import typing

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
        if user:
            supply = Supply()
            inventory = supply.get_supply(user_id=user)
            return JsonResponse({"supply": list(inventory)})
        else:
            return HttpResponse(status=401)


if typing.TYPE_CHECKING:
    from rest_framework.request import Request