from __future__ import annotations

import typing

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


if typing.TYPE_CHECKING:
    from rest_framework.request import Request