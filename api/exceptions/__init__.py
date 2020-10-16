from rest_framework.exceptions import APIException
from rest_framework import status


class Http400(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid Request'
    default_code = 'invalid_request'
