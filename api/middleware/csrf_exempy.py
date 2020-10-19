from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        """
        Override and bypass CSRF enforcement.
        :param request: Request object.
        :return: None
        """
        return
