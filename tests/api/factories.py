from datetime import datetime
from random import randint

import pytz
from factory import Iterator
from factory.django import DjangoModelFactory
from factory.fuzzy import BaseFuzzyDateTime

from datasets.tellus_data import models


class TellingFactory(DjangoModelFactory):
    class Meta:
        model = models.Telling

    tel_richting = Iterator(models.TelRichting.objects.all())
    snelheids_interval = Iterator(models.SnelheidsInterval.objects.all())
    lengte_interval = Iterator(models.LengteInterval.objects.all())

    validatie_categorie = Iterator(models.ValidatieCategorie.objects.all())
    representatief_categorie = Iterator(models.RepresentatiefCategorie.objects.all())
    meetraai_categorie = Iterator(models.MeetraaiCategorie.objects.all())

    tijd_van = BaseFuzzyDateTime(
        start_dt=datetime(2016, 1, 11, 0, 0, 0, 0, pytz.UTC),
        end_dt=datetime.now(pytz.UTC),
    )
    tijd_tot = BaseFuzzyDateTime(
        start_dt=datetime(2016, 1, 11, 0, 0, 0, 0, pytz.UTC),
        end_dt=datetime.now(pytz.UTC),
    )

    aantal = randint(0, 1000)
