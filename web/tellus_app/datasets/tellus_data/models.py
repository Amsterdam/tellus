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
    snelheids_klasse = models.ForeignKey(SnelheidsCategorie, related_name='tellussen')
    standplaats = models.CharField(max_length=80)
    zijstraat_a = models.CharField(max_length=80)
    zijstraat_b = models.CharField(max_length=80)
    richting_1 = models.CharField(max_length=80)
    richting_2 = models.CharField(max_length=80)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rijksdriehoek_x = models.FloatField()
    rijksdriehoek_y = models.FloatField()
    geometrie = models.PointField(null=True, srid=28992)

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

    REPRESENTATIVE = ((0, 'Geen data'),
                      (1, "Representatieve dag"),
                      (2, "Schoolvakantie"),
                      (3, "Feestdag"),
                      (4, "Niet representatieve dag"))

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
    data = models.TextField(null=True)

    def __str__(self):
        return "TellusData {} {}".format(self.tellus, self.tijd_van)

    class Meta:
        unique_together = ("tellus", "richting", "tijd_van", "tijd_tot")
