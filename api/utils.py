from .models.users import User


def get_user_id_from_request(request):
    """
    get the user id from the web app portal key
    :param request: the http request
    :return: the user id
    """
    user = None
    portal_key = request.data.get('portal', None)
    if portal_key is not None:
        user = User.objects.get(portal_firestore_key=portal_key)

    return user.id
