from django.contrib.gis.db import models
from compositefk.fields import CompositeForeignKey


class SnelheidsCategorie(models.Model):
    """
    De snelheidscategorieen worden hier beschreven

    """
    categorie = models.IntegerField(primary_key=True)
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
        return "SnelheidsCategorie {}".format(self.categorie)


class LengteCategorie(models.Model):
    """
    Lengtecategorie
    """
    categorie = models.CharField(max_length=2, primary_key=True, default='X')
    lengte_van = models.CharField(max_length=10, default='0')
    lengte_tot = models.CharField(max_length=10, blank=True, default='')

    def __str__(self):
        return "LengteCategorie {}".format(self.categorie)


class Locatie(models.Model):
    """
    De tellussen die worden geadministreerd worden hier
    gedefinieerd (= Meta info).

    Meta info kan wijzigen. Als dat het geval is, dan wordt
    een NIEUWE tellus aangemaakt, en wordt voor het bestaande
    telpunt een einddatum ingevuld
    """

    meetlocatie = models.IntegerField()
    richting = models.IntegerField(blank=True, null=True)
    telpunt = models.CharField(max_length=256)
    straat = models.CharField(max_length=150)
    windrichting = models.CharField(max_length=20, blank=True, null=True)
    zijstraat1 = models.CharField(max_length=256, blank=True, null=True)
    zijstraat2 = models.CharField(max_length=256, blank=True, null=True)
    richting = models.CharField(max_length=256)
    ingangsdatum = models.DateField(blank=True, null=True)
    eindedatum = models.DateField(blank=True, null=True)
    snelheidscategorie = models.ForeignKey(SnelheidsCategorie, on_delete=models.SET_NULL, null=True)
    lengtecategorie = models.ForeignKey(LengteCategorie, on_delete=models.SET_NULL, null=True)
    geometrie = models.PointField(srid=28992, blank=True, null=True)

    def __str__(self):
        return "Locatie ID: {} meetlocatie/richting: {}/{}".format(
            self.id, self.meetlocatie, self.richting)

    class Meta:
        unique_together = ("meetlocatie", "richting")


class Telling(models.Model):
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

    meetlocatie = models.IntegerField()
    richting = models.IntegerField(blank=True, null=True)
    locatie = CompositeForeignKey(
        Locatie, on_delete=models.CASCADE, related_name='locaties', to_fields={
            "meetlocatie": "meetlocatie",
            "richting": "richting"
        }, nullable_fields=["richting"], default=0
    )
    validatie = models.IntegerField()
    representatief = models.IntegerField()
    meetraai = models.IntegerField()
    classificatie = models.IntegerField()
    tijd_van = models.DateTimeField(auto_now_add=True)
    tijd_tot = models.DateTimeField(auto_now_add=True)
    c1 = models.IntegerField(null=True)
    c2 = models.IntegerField(null=True)
    c3 = models.IntegerField(null=True)
    c4 = models.IntegerField(null=True)
    c5 = models.IntegerField(null=True)
    c6 = models.IntegerField(null=True)
    c7 = models.IntegerField(null=True)
    c8 = models.IntegerField(null=True)
    c9 = models.IntegerField(null=True)
    c10 = models.IntegerField(null=True)
    c11 = models.IntegerField(null=True)
    c12 = models.IntegerField(null=True)
    c13 = models.IntegerField(null=True)
    c14 = models.IntegerField(null=True)
    c15 = models.IntegerField(null=True)
    c16 = models.IntegerField(null=True)
    c17 = models.IntegerField(null=True)
    c18 = models.IntegerField(null=True)
    c19 = models.IntegerField(null=True)
    c20 = models.IntegerField(null=True)
    c21 = models.IntegerField(null=True)
    c22 = models.IntegerField(null=True)
    c23 = models.IntegerField(null=True)
    c24 = models.IntegerField(null=True)
    c25 = models.IntegerField(null=True)
    c26 = models.IntegerField(null=True)
    c27 = models.IntegerField(null=True)
    c28 = models.IntegerField(null=True)
    c29 = models.IntegerField(null=True)
    c30 = models.IntegerField(null=True)
    c31 = models.IntegerField(null=True)
    c32 = models.IntegerField(null=True)
    c33 = models.IntegerField(null=True)
    c34 = models.IntegerField(null=True)
    c35 = models.IntegerField(null=True)
    c36 = models.IntegerField(null=True)
    c37 = models.IntegerField(null=True)
    c38 = models.IntegerField(null=True)
    c39 = models.IntegerField(null=True)
    c40 = models.IntegerField(null=True)
    c41 = models.IntegerField(null=True)
    c42 = models.IntegerField(null=True)
    c43 = models.IntegerField(null=True)
    c44 = models.IntegerField(null=True)
    c45 = models.IntegerField(null=True)
    c46 = models.IntegerField(null=True)
    c47 = models.IntegerField(null=True)
    c48 = models.IntegerField(null=True)
    c49 = models.IntegerField(null=True)
    c50 = models.IntegerField(null=True)
    c51 = models.IntegerField(null=True)
    c52 = models.IntegerField(null=True)
    c53 = models.IntegerField(null=True)
    c54 = models.IntegerField(null=True)
    c55 = models.IntegerField(null=True)
    c56 = models.IntegerField(null=True)
    c57 = models.IntegerField(null=True)
    c58 = models.IntegerField(null=True)
    c59 = models.IntegerField(null=True)
    c60 = models.IntegerField(null=True)

    @property
    def snelheden(self):
        pass

    @property
    def telling_per_lengte(self):
        pass

    @property
    def totaal_telling(self):
        pass
