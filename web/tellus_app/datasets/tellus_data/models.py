from django.contrib.gis.db import models
from django.db.models import CASCADE

DAY_TYPES = (
    ("Weekend", "Weekend"),
    ("Werkdag", "Werkdag")
)


class LengteInterval(models.Model):
    """
    Een lengte interval omvat een bereik van voertuig lengtes.
    Indien de min of max lengte niet is ingevuld dan is het bereik onbegrensd, e.g.: < 3m.
    """
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=40, unique=True)
    min_cm = models.IntegerField(null=True)
    max_cm = models.IntegerField(null=True)

    def __str__(self):
        return "LengteInterval {}: {}".format(self.label, self.label)


class SnelheidsInterval(models.Model):
    """
    Een snelheids interval omvat een bereik van snelheden.
    Indien de min of max snelheid niet is ingevuld dan is het bereik onbegrensd, e.g.: < 30 km/h.
    """
    label = models.CharField(max_length=40, unique=True)
    min_kmph = models.IntegerField(null=True)
    max_kmph = models.IntegerField(null=True)

    def __str__(self):
        return "SnelheidsInterval {}: {}".format(self.id, self.label)


class SnelheidsCategorie(models.Model):
    """
    Snelheids categorieën voor verschillende type wegen.
    e.g.: categorie 1: < 30 km/u, 31 - 40 km/u, ... , 91 - 100 km/u, > 100 km/u
    """
    categorie = models.IntegerField()
    index = models.IntegerField()
    interval = models.ForeignKey(SnelheidsInterval, on_delete=CASCADE)

    def __str__(self):
        return "SnelheidsCategorie {}, s{}: {}".format(self.categorie, self.index, self.interval.label)

    class Meta:
        unique_together = ("categorie", "index", )


class RepresentatiefCategorie(models.Model):
    """
    De representatief categorieën worden hier beschreven
    """
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f"RepresentatiefCategorie {self.id} - {self.label}"


class ValidatieCategorie(models.Model):
    """
    De validatie categorieën worden hier beschreven
    """
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f"ValidatieCategorie {self.id} - {self.label}"


class MeetraaiCategorie(models.Model):
    """
    De meetraai categorieën worden hier beschreven
    """
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=40)

    def __str__(self):
        return f"MeetraaiCategorie {self.id} - {self.label}"


class Meetlocatie(models.Model):
    """
    Een meetlocatie is een plek waar 1 of meer tellussen staan.
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Tellus(models.Model):
    """
    Tellus met leverancier en Vekeer en Openbare Ruimte (vor) nummer.
    """
    objnr_vor = models.CharField(max_length=10, unique=True)
    objnr_leverancier = models.CharField(max_length=10, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rijksdriehoek_x = models.FloatField()
    rijksdriehoek_y = models.FloatField()
    geometrie = models.PointField(null=True, srid=28992)
    snelheids_categorie = models.IntegerField()
    meetlocatie = models.ForeignKey(Meetlocatie, on_delete=CASCADE)

    def __str__(self):
        return "{} - {}".format(self.objnr_leverancier, self.meetlocatie)


class TelRichting(models.Model):
    """
    Tel richting behorende bij een tellus.
    """
    richting = models.IntegerField()
    tellus = models.ForeignKey(Tellus, related_name="tel_richtingen", on_delete=CASCADE)
    naam = models.CharField(max_length=80)
    zijstraat = models.CharField(max_length=80)

    def __str__(self):
        return "{} - {}".format(self.tellus, self.naam)


class Telling(models.Model):
    """
    Telling van een lengte en snelheids interval over een tijdsperiode.
    """
    tel_richting = models.ForeignKey(TelRichting, on_delete=CASCADE)
    snelheids_interval = models.ForeignKey(SnelheidsInterval, on_delete=CASCADE)
    lengte_interval = models.ForeignKey(LengteInterval, on_delete=CASCADE)

    validatie_categorie = models.ForeignKey(ValidatieCategorie, on_delete=CASCADE)
    representatief_categorie = models.ForeignKey(RepresentatiefCategorie, on_delete=CASCADE)
    meetraai_categorie = models.ForeignKey(MeetraaiCategorie, on_delete=CASCADE)

    tijd_van = models.DateTimeField()
    tijd_tot = models.DateTimeField()

    aantal = models.IntegerField()

    def __str__(self):
        return "{} - van {} tot {}: {}".format(
            self.tel_richting, self.tijd_van.strftime('%d-%m-%Y %H:%M'), self.tijd_tot.strftime('%H:%M'), self.aantal)

    class Meta:
        ordering = ['id', 'tijd_van', 'tijd_tot']
        unique_together = ("tel_richting", "tijd_van", "tijd_tot", "snelheids_interval", "lengte_interval")


class TellusDataCarsPerHourPerDay(models.Model):
    """
    Aggregated Model for:
    - Every Tellus
    - Every day
    - Every hour
    - Type of day
    - Sum of all cars passing within that hour slot (merge speeds and lengtes)
    """
    id = models.IntegerField(primary_key=True)
    tellus = models.ForeignKey(Tellus, on_delete=CASCADE)
    richting_id = models.IntegerField()
    dag_uur = models.DateTimeField()  # Start of hourly time window
    dag_type = models.CharField(max_length=80, choices=DAY_TYPES)
    aantal = models.IntegerField()

    # Disallow changes to this database through Django ORM!
    def save(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError

    def __str__(self):
        return "{} 1 uur lang vanaf {} op dag {} gemeten".format(
            self.tel_richting,
            self.dag_uur.strftime('%H:%M'),
            self.dag_uur.strftime('%d-%m-%Y'))

    class Meta:
        managed = False
        db_table = 'tellus_data_cars_per_hour'


class TellusDataCarsPerHourLength(models.Model):  # TODO: try to get inheritance working
    """
    Aggregated Model for:
    - Every Tellus
    - Every day
    - Every hour
    - Every length
    - Type of day
    - Sum of all cars passing within that hour slot (merge speeds)
    """
    id = models.IntegerField(primary_key=True)
    tellus = models.ForeignKey(Tellus, on_delete=CASCADE)
    richting_id = models.IntegerField()
    dag_uur = models.DateTimeField()  # Start of hourly time window
    dag_type = models.CharField(max_length=80, choices=DAY_TYPES)
    lengte_interval = models.ForeignKey(LengteInterval, on_delete=CASCADE)
    label = models.CharField(max_length=40, unique=True)
    aantal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tellus_data_cars_per_hour_length'


class TellusDataCarsPerHourSpeed(models.Model):
    """
    Aggregated Model for:
    - Every Tellus
    - Every day
    - Every hour
    - Every speed
    - Type of day
    - Sum of all cars passing within that hour slot (merge lengths)
    """
    id = models.IntegerField(primary_key=True)
    tellus = models.ForeignKey(Tellus, on_delete=CASCADE)
    richting_id = models.IntegerField()
    dag_uur = models.DateTimeField()  # Start of hourly time window
    dag_type = models.CharField(max_length=80, choices=DAY_TYPES)
    snelheids_interval = models.ForeignKey(SnelheidsInterval, on_delete=CASCADE)
    label = models.CharField(max_length=40, unique=True)
    aantal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tellus_data_cars_per_hour_speed'
