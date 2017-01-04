from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField


class SnelheidsCategorieen(models.Model):
    """
    De snelheidscategorieen worden hier beschreven

    """
    snelheden = JSONField()


class LengteCategorieen(models.Model):
    """
    Lengtecategorieen zijn hier beschreven

    """
    lengtes = JSONField()


class TellusInfo(models.Model):
    """
    De tellussen die worden geadministreerd worden hier
    gedefinieerd (= Meta info).

    Meta info kan wijzigen. Als dat het geval is, dan wordt
    een NIEUWE tellus aangemaakt, en wordt voor het bestaande
    telpunt een einddatum ingevuld
    """

    telpunt = models.CharField(max_length=256)
    meetlocatie = models.IntegerField()
    richtingcode = models.IntegerField(blank=True, null=True)
    straat = models.CharField(max_length=150)
    windrichting = models.CharField(max_length=20, blank=True, null=True)
    zijstraat1 = models.CharField(max_length=256, blank=True, null=True)
    zijstraat2 = models.CharField(max_length=256, blank=True, null=True)
    richting = models.CharField(max_length=256)
    ingangsdatum = models.DateField(blank=True, null=True)
    eindedatum = models.DateField(blank=True, null=True)
    snelheidscategorie = models.ForeignKey(SnelheidsCategorieen, on_delete=models.SET_NULL, null=True)
    lengtecategorie = models.ForeignKey(LengteCategorieen, on_delete=models.SET_NULL, null=True)
    geometrie = models.PointField(srid=28992, blank=True, null=True)


class Tellingen(models.Model):
    """
    De tellingen per lus
    NB. omdat per richting er een TellusInfo bestaat is de richting
    hier niet nodig.
    Meetlocatie;Richting;Validatie;Representatief;Meetraai;Classificatie;Tijd_Van;Tijd_Tot;
    C1;C2;C3;C4;C5;C6;C7;C8;C9;C10;C11;C12;C13;C14;C15;
    C16;C17;C18;C19;C20;C21;C22;C23;C24;C25;C26;C27;C28;C29;C30;
    C31;C32;C33;C34;C35;C36;C37;C38;C39;C40;C41;C42;C43;C44;C45;
    C46;C47;C48;C49;C50;C51;C52;C53;C54;C55;C56;C57;C58;C59;C60;
    """
    meetlocatie = models.ForeignKey(TellusInfo, on_delete=models.CASCADE)
    richting = models.IntegerField()
    validatie = models.IntegerField()
    representatief = models.IntegerField()
    meetraai = models.IntegerField()
    classificatie = models.IntegerField()
    tijd_Van = models.DateTimeField()
    tijd_Tot = models.DateTimeField
    c1 = models.IntegerField()
    c2 = models.IntegerField()
    c3 = models.IntegerField()
    c4 = models.IntegerField()
    c5 = models.IntegerField()
    c6 = models.IntegerField()
    c7 = models.IntegerField()
    c8 = models.IntegerField()
    c9 = models.IntegerField()
    c10 = models.IntegerField()
    c11 = models.IntegerField()
    c12 = models.IntegerField()
    c13 = models.IntegerField()
    c14 = models.IntegerField()
    c15 = models.IntegerField()
    c16 = models.IntegerField()
    c17 = models.IntegerField()
    c18 = models.IntegerField()
    c19 = models.IntegerField()
    c20 = models.IntegerField()
    c21 = models.IntegerField()
    c22 = models.IntegerField()
    c23 = models.IntegerField()
    c24 = models.IntegerField()
    c25 = models.IntegerField()
    c26 = models.IntegerField()
    c27 = models.IntegerField()
    c28 = models.IntegerField()
    c29 = models.IntegerField()
    c30 = models.IntegerField()
    c31 = models.IntegerField()
    c32 = models.IntegerField()
    c33 = models.IntegerField()
    c34 = models.IntegerField()
    c35 = models.IntegerField()
    c36 = models.IntegerField()
    c37 = models.IntegerField()
    c38 = models.IntegerField()
    c39 = models.IntegerField()
    c40 = models.IntegerField()
    c41 = models.IntegerField()
    c42 = models.IntegerField()
    c43 = models.IntegerField()
    c44 = models.IntegerField()
    c45 = models.IntegerField()
    c46 = models.IntegerField()
    c47 = models.IntegerField()
    c48 = models.IntegerField()
    c49 = models.IntegerField()
    c50 = models.IntegerField()
    c51 = models.IntegerField()
    c52 = models.IntegerField()
    c53 = models.IntegerField()
    c54 = models.IntegerField()
    c55 = models.IntegerField()
    c56 = models.IntegerField()
    c57 = models.IntegerField()
    c58 = models.IntegerField()
    c59 = models.IntegerField()
    c60 = models.IntegerField()

    @property
    def snelheden(self):
        pass

    @property
    def telling_per_lengte(self):
        pass

    @property
    def totaal_telling(self):
        pass
