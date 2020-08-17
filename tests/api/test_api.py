"""Tests
"""

import logging

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from datasets.tellus_data.models import (
    LengteInterval,
    Meetlocatie,
    SnelheidsInterval,
    Telling,
    Tellus,
    TelRichting,
)
from tests.api.authzsetup import AuthorizationSetup
from tests.api.factories import TellingFactory

log = logging.getLogger(__name__)


class TestAPIEndpoints(APITestCase, AuthorizationSetup):
    """
    Verifies that browsing the API works correctly.
    """

    fixtures = [
        "meetlocatie.json",
        "lengte_interval.json",
        "snelheids_interval.json",
        "representatief_categorie.json",
        "validatie_categorie.json",
        "meetraai_categorie.json",
        "tellus.json",
        "tel_richting.json",
    ]

    reverse_list_urls = [
        "meetlocatie-list",
        "lengteinterval-list",
        "snelheidsinterval-list",
        "representatiefcategorie-list",
        "validatiecategorie-list",
        "meetraaicategorie-list",
        "tellus-list",
        "telrichting-list",
        "telling-list",
    ]
    reverse_detail_urls = [
        "tellus-detail",
        # 'meetlocatie-detail',
        "lengteinterval-detail",
        "snelheidsinterval-detail",
        "representatiefcategorie-detail",
        "validatiecategorie-detail",
        "meetraaicategorie-detail",
        "tellus-detail",
        "telrichting-detail",
        "telling-detail",
    ]

    def setUp(self):
        TellingFactory.create_batch(1000)
        self.setUpAuthorization()

    def valid_response(self, url, response):
        """
        Helper method to check common status/json
        """

        self.assertEqual(
            200, response.status_code, "Wrong response code for {}".format(url)
        )

        self.assertEqual(
            "application/json",
            response["Content-Type"],
            "Wrong Content-Type for {}".format(url),
        )

    def test_setup(self):
        self.assertEqual(LengteInterval.objects.count(), 6)
        self.assertEqual(SnelheidsInterval.objects.count(), 20)
        self.assertEqual(Meetlocatie.objects.count(), 26)
        self.assertEqual(Tellus.objects.count(), 30)
        self.assertEqual(TelRichting.objects.count(), 51)
        self.assertEqual(Telling.objects.count(), 1000)

    def test_lists(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(self.token_scope_tlls_r)
        )

        for url in self.reverse_list_urls:
            log.debug("test {} => {}".format(url, reverse(url)))
            response = self.client.get(reverse(url))
            self.valid_response(url, response)
            self.assertIn(
                "count", response.data, "No count attribute in {}".format(url)
            )
            self.assertGreater(
                response.data["count"], 0, "Wrong result count for {}".format(url)
            )

    def test_details(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(self.token_scope_tlls_r)
        )

        for url in self.reverse_detail_urls:
            log.debug("test {} => {}".format(url, reverse(url, [1])))
            self.valid_response(url, self.client.get(reverse(url, [1])))
