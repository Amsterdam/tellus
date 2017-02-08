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
    c1 = randint(0, 1000)
    c2 = randint(0, 1000)
    c3 = randint(0, 1000)
    c4 = randint(0, 1000)
    c5 = randint(0, 1000)
    c6 = randint(0, 1000)
    c7 = randint(0, 1000)
    c8 = randint(0, 1000)
    c9 = randint(0, 1000)
    c10 = randint(0, 1000)
    c11 = randint(0, 1000)
    c12 = randint(0, 1000)
    c13 = randint(0, 1000)
    c14 = randint(0, 1000)
    c15 = randint(0, 1000)
    c16 = randint(0, 1000)
    c17= randint(0, 1000)
    c18 = randint(0, 1000)
    c19 = randint(0, 1000)
    c20 = randint(0, 1000)
    c21 = randint(0, 1000)
    c22 = randint(0, 1000)
    c23 = randint(0, 1000)
    c24 = randint(0, 1000)
    c25 = randint(0, 1000)
    c26 = randint(0, 1000)
    c27= randint(0, 1000)
    c28 = randint(0, 1000)
    c29 = randint(0, 1000)
    c30 = randint(0, 1000)
    c31 = randint(0, 1000)
    c32 = randint(0, 1000)
    c33 = randint(0, 1000)
    c34 = randint(0, 1000)
    c35 = randint(0, 1000)
    c36 = randint(0, 1000)
    c37= randint(0, 1000)
    c38 = randint(0, 1000)
    c39 = randint(0, 1000)
    c40 = randint(0, 1000)
    c41 = randint(0, 1000)
    c42 = randint(0, 1000)
    c43 = randint(0, 1000)
    c44 = randint(0, 1000)
    c45 = randint(0, 1000)
    c46 = randint(0, 1000)
    c47= randint(0, 1000)
    c48 = randint(0, 1000)
    c49 = randint(0, 1000)
    c50 = randint(0, 1000)
    c51 = randint(0, 1000)
    c52 = randint(0, 1000)
    c53 = randint(0, 1000)
    c54 = randint(0, 1000)
    c55 = randint(0, 1000)
    c56 = randint(0, 1000)
    c57= randint(0, 1000)
    c58 = randint(0, 1000)
    c59 = randint(0, 1000)
    c60 = randint(0, 1000)
