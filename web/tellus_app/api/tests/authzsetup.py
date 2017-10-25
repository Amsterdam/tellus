import time
import jwt

from django.conf import settings

from authorization_django import levels as authorization_levels


class AuthorizationSetup(object):
    """
    Helper methods to setup JWT tokens and authorization levels

    sets the following attributes:

    token_scope_tlls_r
    """

    def setUpAuthorization(self):
        """
        SET

        token_scope_ttls_r

        to use with:

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_scope_tlls_R))

        """
        # NEW STYLE AUTH
        key = 'thisisatestkey!!!!'
        settings.DATAPUNT_AUTHZ['JWT_SECRET_KEY'] = key
        algorithm = settings.DATAPUNT_AUTHZ['JWT_ALGORITHM']

        now = int(time.time())

        token_scope_tlls_r = jwt.encode({
            'scopes': [authorization_levels.SCOPE_TLLS_R],
            'iat': now, 'exp': now + 600}, key, algorithm=algorithm)

        self.token_scope_tlls_r = str(token_scope_tlls_r, 'utf-8')
