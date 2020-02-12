import time

from jwcrypto.jwt import JWT

import authorization_levels
from authorization_django.jwks import get_keyset


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
        jwks = get_keyset()
        assert len(jwks['keys']) > 0

        key = next(iter(jwks['keys']))
        now = int(time.time())

        header = {
            'alg': 'ES256',  # algorithm of the test key
            'kid': key.key_id
        }

        token = JWT(
            header=header,
            claims={
                'iat': now,
                'exp': now + 600,
                'scopes': [authorization_levels.SCOPE_TLLS_R]
            }
        )
        token.make_signed_token(key)
        self.token_scope_tlls_r = token.serialize()
