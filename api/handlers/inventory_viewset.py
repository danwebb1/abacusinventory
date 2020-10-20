from __future__ import annotations

import typing
from django.shortcuts import render
from ..definitions import GET, POST
from rest_framework.decorators import action
from api.models.inventory import Supply, Item, Upc, UpcList, UpcMap
from rest_framework import viewsets
from rest_framework.response import Response


class InventoryViewSet(viewsets.ViewSet):
    def list(self, request: Request):
        return Response('test')


if typing.TYPE_CHECKING:
    from rest_framework.request import Request