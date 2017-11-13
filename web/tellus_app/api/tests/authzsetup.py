import time
import jwt

from django.conf import settings
from authorization_django.config import settings as middleware_settings

import authorization_levels


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
        # VERY NEW STYLE AUTH
        # The following JWKS data was obtained in the authz project :  jwkgen -create -alg ES256
        # This is a test private/public key pair.
        settings.DATAPUNT_AUTHZ['JWKS'] = """
            {
                "keys": [
                    {
                        "kty": "EC",
                        "key_ops": [
                            "verify",
                            "sign"
                        ],
                        "kid": "2aedafba-8170-4064-b704-ce92b7c89cc6",
                        "crv": "P-256",
                        "x": "6r8PYwqfZbq_QzoMA4tzJJsYUIIXdeyPA27qTgEJCDw=",
                        "y": "Cf2clfAfFuuCB06NMfIat9ultkMyrMQO9Hd2H7O9ZVE=",
                        "d": "N1vu0UQUp0vLfaNeM0EDbl4quvvL6m_ltjoAXXzkI3U="
                    }
                ]
            }
        """
        jwks = middleware_settings()['JWKS'].signers

        assert len(jwks) > 0
        (kid, key), = jwks.items()

        now = int(time.time())

        token_scope_tlls_r = jwt.encode({
            'scopes': [authorization_levels.SCOPE_TLLS_R],
            'iat': now, 'exp': now + 600}, key.key, algorithm=key.alg,
             headers={'kid': kid})

        self.token_scope_tlls_r = str(token_scope_tlls_r, 'utf-8')
