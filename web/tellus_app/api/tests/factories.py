from datetime import datetime
from random import randint

import factory
import pytz
from factory import fuzzy

from datasets.tellus_data import models


class TellingFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Telling

    tel_richting = factory.Iterator(models.TelRichting.objects.all())
    snelheids_interval = factory.Iterator(models.SnelheidsInterval.objects.all())
    lengte_interval = factory.Iterator(models.LengteInterval.objects.all())

    validatie_categorie = factory.Iterator(models.ValidatieCategorie.objects.all())
    representatief_categorie = factory.Iterator(models.RepresentatiefCategorie.objects.all())
    meetraai_categorie = factory.Iterator(models.MeetraaiCategorie.objects.all())

    tijd_van = fuzzy.BaseFuzzyDateTime(
        start_dt=datetime(2016, 1, 11, 0, 0, 0, 0, pytz.UTC),
        end_dt=datetime.now(pytz.UTC))
    tijd_tot = fuzzy.BaseFuzzyDateTime(
        start_dt=datetime(2016, 1, 11, 0, 0, 0, 0, pytz.UTC),
        end_dt=datetime.now(pytz.UTC))

    aantal = randint(0, 1000)
