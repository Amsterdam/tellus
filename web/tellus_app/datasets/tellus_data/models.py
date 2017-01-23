from django.contrib.gis.db import models


class SnelheidsKlasse(models.Model):
    """
    De snelheidsklasse worden hier beschreven
    """
    klasse = models.IntegerField(primary_key=True)
    s1 = models.CharField(max_length=30, default='nvt')
    s2 = models.CharField(max_length=30, default='nvt')
    s3 = models.CharField(max_length=30, default='nvt')
    s4 = models.CharField(max_length=30, default='nvt')
    s5 = models.CharField(max_length=30, default='nvt')
    s6 = models.CharField(max_length=30, default='nvt')
    s7 = models.CharField(max_length=30, default='nvt')
    s8 = models.CharField(max_length=30, default='nvt')
    s9 = models.CharField(max_length=30, default='nvt')
    s10 = models.CharField(max_length=30, default='nvt')

    def __str__(self):
        return "SnelheidsKlasse {}".format(self.klasse)


class Tellus(models.Model):
    """
    De geadministreerde tellussen die worden worden hier
    gedefinieerd (= Meta info).

    Meta info kan wijzigen. Als dat het geval is, dan wordt
    een NIEUWE tellus aangemaakt, en wordt voor het bestaande
    telpunt een einddatum ingevuld
    """

    objnr_vor = models.CharField(max_length=10, unique=True)
    objnr_leverancier = models.CharField(max_length=10, unique=True)
    snelheids_klasse = models.ForeignKey(SnelheidsKlasse, related_name='tellussen')
    standplaats = models.CharField(max_length=80)
    zijstraat_a = models.CharField(max_length=80)
    zijstraat_b = models.CharField(max_length=80)
    richting_1 = models.CharField(max_length=80)
    richting_2 = models.CharField(max_length=80)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rijksdriehoek_x = models.FloatField()
    rijksdriehoek_y = models.FloatField()

    def __str__(self):
        return "Tellus {}".format(self.objnr_vor)


class TellusData(models.Model):
    """
    De tellingen per lus
    """
    VALIDATION_CHOICES = ((0, "Geen data"),
                          (1, "Consistent, plausibel 100% compleet"),
                          (2, "Consistent, plausibel >98% compleet"),
                          (3, "Consistent, plausibel <98% compleet"),
                          (4, "Niet consistent"),
                          (5, "Niet plausibel"))

    LENGTH_CATEGORY = (('L1', '0 - 5,1m'),
                       ('L2', '5,1 - 5,6m'),
                       ('L3', '5,6 - 7,5m'),
                       ('L4', '7,5 - 10,5m'),
                       ('L5', '10,5 - 12,2m'),
                       ('L6', '>12,2m'))

    REPRESENTATIVE = ((0, 'Geen data'),
                      (1, "Representatieve dag"),
                      (2, "Schoolvakantie"),
                      (3, "Feestdag"),
                      (4, "Niet representatieve dag"))

    MEETRAAI = ((0, "Niet compleet"),
                (1, "Compleet"),
                (2, "Niet compleet, data wel bruikbaar"))

    tellus = models.ForeignKey(Tellus)
    tijd_van = models.DateTimeField()
    tijd_tot = models.DateTimeField()
    richting = models.IntegerField()
    validatie = models.IntegerField(choices=VALIDATION_CHOICES)
    lengte_categorie = models.CharField(max_length=20, choices=LENGTH_CATEGORY)
    representatief = models.IntegerField(choices=REPRESENTATIVE)
    meetraai = models.IntegerField(choices=MEETRAAI)
    meting_1 = models.IntegerField(default=0)
    meting_2 = models.IntegerField(default=0)
    meting_3 = models.IntegerField(default=0)
    meting_4 = models.IntegerField(default=0)
    meting_5 = models.IntegerField(default=0)
    meting_6 = models.IntegerField(default=0)
    meting_7 = models.IntegerField(default=0)
    meting_8 = models.IntegerField(default=0)
    meting_9 = models.IntegerField(default=0)
    meting_10 = models.IntegerField(default=0)

    def __str__(self):
        return "TellusData {} {}".format(self.tellus, self.tijd_van)

    @property
    def snelheids_klasse(self):
        return self.tellus.snelheids_klasse
