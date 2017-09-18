from django.contrib.gis.db import models


class LengteCategorie(models.Model):
    """
    De lengte categorieen worden hier beschreven
    """
    klasse = models.IntegerField(primary_key=True)
    l1 = models.CharField(max_length=30, default='')
    l2 = models.CharField(max_length=30, default='')
    l3 = models.CharField(max_length=30, default='')
    l4 = models.CharField(max_length=30, default='')
    l5 = models.CharField(max_length=30, default='')
    l6 = models.CharField(max_length=30, default='')

    def __str__(self):
        return "LengteCategorie {}".format(self.klasse)


class SnelheidsCategorie(models.Model):
    """
    De snelheids categorieen worden hier beschreven
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
        return "SnelheidsCategorie {}".format(self.klasse)


class RepresentatiefCategorie(models.Model):
    """
    De snelheids categorieen worden hier beschreven
    """
    representatief = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=40, default='nvt')

    def __str__(self):
        return f"RepresentatiefCategorie {self.representatief} - {self.label}"


class ValidatieCategorie(models.Model):
    """
    De snelheids categorieen worden hier beschreven
    """
    validatie = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=40, default='nvt')

    def __str__(self):
        return f"ValidatieCategorie {self.validatie} - {self.label}"


class MeetraaiCategorie(models.Model):
    """
    De snelheids categorieen worden hier beschreven
    """
    meetraai = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=40, default='nvt')

    def __str__(self):
        return f"MeetraaiCategorie {self.meetraai} - {self.label}"


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
    snelheids_klasse = models.ForeignKey(SnelheidsCategorie,
                                         related_name='tellussen',
                                         null=True)
    standplaats = models.CharField(max_length=80)
    zijstraat_a = models.CharField(max_length=80)
    zijstraat_b = models.CharField(max_length=80)
    richting_1 = models.CharField(max_length=80)
    richting_2 = models.CharField(max_length=80)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    rijksdriehoek_x = models.FloatField(null=True)
    rijksdriehoek_y = models.FloatField(null=True)
    geometrie = models.PointField(null=True, srid=28992)

    def __str__(self):
        return "{} - {}".format(self.objnr_leverancier, self.standplaats)


class TellusData(models.Model):
    """
    De tellingen per lus
    C1 tot C60 zijn de geaggregeerde meetwaarden zoals ze per CSV aangeleverd worden door `Dufec`
    Het 60 kolommen van (6 x 10) meetwaarden, lengtecategorie x snelheidscategorie.
    In de pivot views worden deze verder gereed gemaakt vor verwerking met oa. `Tableau`
    """
    VALIDATION_CHOICES = ((0, "Geen data"),
                          (1, "Consistent, plausibel 100% compleet"),
                          (2, "Consistent, plausibel >98% compleet"),
                          (3, "Consistent, plausibel <98% compleet"),
                          (4, "Niet consistent"),
                          (5, "Niet plausibel"))

    REPRESENTATIVE = ((0, 'Geen data'),
                      (1, "Representatieve dag"),
                      (2, "Schoolvakantie"),
                      (3, "Feestdag"),
                      (4, "Niet representatieve dag"),
                      (5, "data/onjuist onbruikbaar")
                      )

    MEETRAAI = ((0, "Niet compleet"),
                (1, "Compleet"),
                (2, "Niet compleet, data wel bruikbaar"))

    tellus = models.ForeignKey(Tellus)
    snelheids_categorie = models.ForeignKey(SnelheidsCategorie)
    lengte_categorie = models.ForeignKey(LengteCategorie)

    tijd_van = models.DateTimeField()
    tijd_tot = models.DateTimeField()
    richting = models.IntegerField()
    validatie = models.IntegerField(choices=VALIDATION_CHOICES)
    representatief = models.IntegerField(choices=REPRESENTATIVE)
    meetraai = models.IntegerField(choices=MEETRAAI)
    c1 = models.IntegerField(null=False, blank=False, default=0)
    c2 = models.IntegerField(null=False, blank=False, default=0)
    c3 = models.IntegerField(null=False, blank=False, default=0)
    c4 = models.IntegerField(null=False, blank=False, default=0)
    c5 = models.IntegerField(null=False, blank=False, default=0)
    c6 = models.IntegerField(null=False, blank=False, default=0)
    c7 = models.IntegerField(null=False, blank=False, default=0)
    c8 = models.IntegerField(null=False, blank=False, default=0)
    c9 = models.IntegerField(null=False, blank=False, default=0)
    c10 = models.IntegerField(null=False, blank=False, default=0)
    c11 = models.IntegerField(null=False, blank=False, default=0)
    c12 = models.IntegerField(null=False, blank=False, default=0)
    c13 = models.IntegerField(null=False, blank=False, default=0)
    c14 = models.IntegerField(null=False, blank=False, default=0)
    c15 = models.IntegerField(null=False, blank=False, default=0)
    c16 = models.IntegerField(null=False, blank=False, default=0)
    c17 = models.IntegerField(null=False, blank=False, default=0)
    c18 = models.IntegerField(null=False, blank=False, default=0)
    c19 = models.IntegerField(null=False, blank=False, default=0)
    c20 = models.IntegerField(null=False, blank=False, default=0)
    c21 = models.IntegerField(null=False, blank=False, default=0)
    c22 = models.IntegerField(null=False, blank=False, default=0)
    c23 = models.IntegerField(null=False, blank=False, default=0)
    c24 = models.IntegerField(null=False, blank=False, default=0)
    c25 = models.IntegerField(null=False, blank=False, default=0)
    c26 = models.IntegerField(null=False, blank=False, default=0)
    c27 = models.IntegerField(null=False, blank=False, default=0)
    c28 = models.IntegerField(null=False, blank=False, default=0)
    c29 = models.IntegerField(null=False, blank=False, default=0)
    c30 = models.IntegerField(null=False, blank=False, default=0)
    c31 = models.IntegerField(null=False, blank=False, default=0)
    c32 = models.IntegerField(null=False, blank=False, default=0)
    c33 = models.IntegerField(null=False, blank=False, default=0)
    c34 = models.IntegerField(null=False, blank=False, default=0)
    c35 = models.IntegerField(null=False, blank=False, default=0)
    c36 = models.IntegerField(null=False, blank=False, default=0)
    c37 = models.IntegerField(null=False, blank=False, default=0)
    c38 = models.IntegerField(null=False, blank=False, default=0)
    c39 = models.IntegerField(null=False, blank=False, default=0)
    c40 = models.IntegerField(null=False, blank=False, default=0)
    c41 = models.IntegerField(null=False, blank=False, default=0)
    c42 = models.IntegerField(null=False, blank=False, default=0)
    c43 = models.IntegerField(null=False, blank=False, default=0)
    c44 = models.IntegerField(null=False, blank=False, default=0)
    c45 = models.IntegerField(null=False, blank=False, default=0)
    c46 = models.IntegerField(null=False, blank=False, default=0)
    c47 = models.IntegerField(null=False, blank=False, default=0)
    c48 = models.IntegerField(null=False, blank=False, default=0)
    c49 = models.IntegerField(null=False, blank=False, default=0)
    c50 = models.IntegerField(null=False, blank=False, default=0)
    c51 = models.IntegerField(null=False, blank=False, default=0)
    c52 = models.IntegerField(null=False, blank=False, default=0)
    c53 = models.IntegerField(null=False, blank=False, default=0)
    c54 = models.IntegerField(null=False, blank=False, default=0)
    c55 = models.IntegerField(null=False, blank=False, default=0)
    c56 = models.IntegerField(null=False, blank=False, default=0)
    c57 = models.IntegerField(null=False, blank=False, default=0)
    c58 = models.IntegerField(null=False, blank=False, default=0)
    c59 = models.IntegerField(null=False, blank=False, default=0)
    c60 = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return "{} - {} van {} tot {}".format(
            self.tellus, self.richting, self.tijd_van.strftime('%d-%m-%Y %H:%M'), self.tijd_tot.strftime('%H:%M'))

    class Meta:
        unique_together = ("tellus", "richting", "tijd_van", "tijd_tot")
