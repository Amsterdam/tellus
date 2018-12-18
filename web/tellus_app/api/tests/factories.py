from datetime import datetime
from random import randint

import factory
import pytz
from factory import fuzzy

from datasets.tellus_data import models

class TellingFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Telling

    id = 1
    tel_richting = factory.Iterator(models.TelRichting.objects.all())
    # snelheids_categorie_id = 1
    # lengte_interval = factory.SubFactory(LengteIntervalFactory)

    tijd_van = fuzzy.BaseFuzzyDateTime(
        start_dt=datetime(2016, 1, 11, 0, 0, 0, 0, pytz.UTC),
        end_dt=datetime.now(pytz.UTC))
    tijd_tot = fuzzy.BaseFuzzyDateTime(
        start_dt=datetime(2016, 1, 11, 0, 0, 0, 0, pytz.UTC),
        end_dt=datetime.now(pytz.UTC))
    richting = fuzzy.FuzzyChoice(choices=(1, 2))
    validatie = 1  # fuzzy.FuzzyChoice(choices=models.TellusData.VALIDATION_CHOICES)
    representatief = 1  # fuzzy.FuzzyChoice(choices=models.TellusData.REPRESENTATIVE)
    meetraai = 1  # fuzzy.FuzzyChoice(choices=models.TellusData.MEETRAAI)
    aantal = randint(0, 1000)

