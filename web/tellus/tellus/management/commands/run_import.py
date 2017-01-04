"""
All commands to create a functioning tellus api dataset
"""

import logging

from django.core.management import BaseCommand

from datasets import build_tellus_data
from datasets import build_meta_data
from datasets.tellus import models


LOG = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Import tellus data from delivered by Dufec

    clear data using:

    - manage.py migrate tellus zero

    apply new/updated migrations

    - manage.py migrate tellus

    """

    def add_arguments(self, parser):
        parser.add_argument(
            '--maandfile',
            action='store_true',
            dest='tellusmaand',
            default=False,
            help='Fill tellus information per month')

        parser.add_argument(
            '--tellusmeta',
            action='store_true',
            dest='meta',
            default=False,
            help='Fill tellus meta data')

    def handle(self, *args, **options):
        """
        validate and execute import task
        """
        LOG.info('Tellus import started')

        if options['tellusmaand']:
            # load bag data in GeoVBO with
            # copy_bag_to_hr script
            build_tellus_data.fill()
            location_stats.log_rapport_counts(action='tellusmaand')
        elif options['meta']:
            build_meta_data.fill()
            location_stats.log_rapport_counts(action='meta')
