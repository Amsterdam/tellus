import logging
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from api.tests.factories import TellusDataFactory
from api.tests.authzsetup import AuthorizationSetup

log = logging.getLogger(__name__)


class TestAPIEndpoints(APITestCase, AuthorizationSetup):
    """
    Verifies that browsing the API works correctly.
    """

    reverse_list_urls = [
        # 'docs',
        'tellus-list',
        'lengtecategorie-list',
        'snelheidcategorie-list',
        'tellusdata-list',
    ]
    reverse_detail_urls = [
        'tellus-detail',
        'lengtecategorie-detail',
        'snelheidscategorie-detail',
        'tellusdata-detail',
    ]

    def setUp(self):
        TellusDataFactory.create()
        self.setUpAuthorization()


    def valid_response(self, url, response):
        """
        Helper method to check common status/json
        """

        self.assertEqual(
            200, response.status_code,
            'Wrong response code for {}'.format(url))

        self.assertEqual(
            'application/json', response['Content-Type'],
            'Wrong Content-Type for {}'.format(url))

    def valid_html_response(self, url, response):
        """
        Helper method to check common status/json
        """

        self.assertEqual(
            200, response.status_code,
            'Wrong response code for {}'.format(url))

        self.assertEqual(
            'text/html; charset=utf-8', response['Content-Type'],
            'Wrong Content-Type for {}'.format(url))

    def test_lists_employee(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_employee))

        for url in self.reverse_list_urls:
            log.debug("test {} => {}".format(url, reverse(url)))
            response = self.client.get(reverse(url))
            self.valid_response(url, response)
            self.assertIn(
                'count', response.data, 'No count attribute in {}'.format(url))
            self.assertNotEqual(
                response.data['count'],
                0, 'Wrong result count for {}'.format(url))

    def test_lists_employee_plus(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_employee_plus))

        for url in self.reverse_list_urls:
            log.debug("test {} => {}".format(url, reverse(url)))
            response = self.client.get(reverse(url))
            self.valid_response(url, response)
            self.assertIn(
                'count', response.data, 'No count attribute in {}'.format(url))
            self.assertNotEqual(
                response.data['count'],
                0, 'Wrong result count for {}'.format(url))

    def test_details_employee(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_employee))

        for url in self.reverse_detail_urls:
            log.debug("test {} => {}".format(url, reverse(url, [1])))
            self.valid_response(url, self.client.get(reverse(url, [1])))

    def test_details_employee_plus(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token_employee_plus))

        for url in self.reverse_detail_urls:
            log.debug("test {} => {}".format(url, reverse(url, [1])))
            self.valid_response(url, self.client.get(reverse(url, [1])))
