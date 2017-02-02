import json
from datetime import datetime
from random import randint

import factory
import pytz
from factory import fuzzy

from datasets.tellus_data import models


class LengteCategorieFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.LengteCategorie

    klasse = 1
    l1 = fuzzy.FuzzyText(length=10)
    l2 = fuzzy.FuzzyText(length=10)
    l3 = fuzzy.FuzzyText(length=10)
    l4 = fuzzy.FuzzyText(length=10)
    l5 = fuzzy.FuzzyText(length=10)
    l6 = fuzzy.FuzzyText(length=10)


class SnelheidsCategorieFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.SnelheidsCategorie

    klasse = 1
    s1 = fuzzy.FuzzyText(length=10)
    s2 = fuzzy.FuzzyText(length=10)
    s3 = fuzzy.FuzzyText(length=10)
    s4 = fuzzy.FuzzyText(length=10)
    s5 = fuzzy.FuzzyText(length=10)
    s6 = fuzzy.FuzzyText(length=10)
    s7 = fuzzy.FuzzyText(length=10)
    s8 = fuzzy.FuzzyText(length=10)
    s9 = fuzzy.FuzzyText(length=10)
    s10 = fuzzy.FuzzyText(length=10)


class TellusFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Tellus

    id = 1
    objnr_vor = 'TP0001'
    objnr_leverancier = 'AMST0001'
    snelheids_klasse = factory.SubFactory(SnelheidsCategorieFactory)
    standplaats = fuzzy.FuzzyText(length=30)
    zijstraat_a = fuzzy.FuzzyText(length=30)
    zijstraat_b = fuzzy.FuzzyText(length=30)
    richting_1 = 1
    richting_2 = 2
    latitude = fuzzy.FuzzyFloat(low=0.0)
    longitude = fuzzy.FuzzyFloat(low=0.0)
    rijksdriehoek_x = fuzzy.FuzzyFloat(low=0.0)
    rijksdriehoek_y = fuzzy.FuzzyFloat(low=0.0)


class TellusDataFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.TellusData

    id = 1
    tellus = factory.SubFactory(TellusFactory)
    snelheids_categorie_id = 1
    lengte_categorie = factory.SubFactory(LengteCategorieFactory)

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
    data = json.dumps([randint(0, 1000) for x in range(60)])
