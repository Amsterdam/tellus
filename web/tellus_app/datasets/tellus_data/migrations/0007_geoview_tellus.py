from django.db import migrations
from django.contrib.sites.models import Site

from tellus import settings

API_DOMAIN = 'API Domain'


def create_site(apps, *args, **kwargs):
    Site.objects.filter(name='API Domain').delete()

    Site.objects.update_or_create(
        domain=settings.DATAPUNT_API_URL,
        name=API_DOMAIN
    )


def delete_site(apps, *args, **kwargs):
    Site.objects.filter(name='API Domain').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('tellus_data', '0006_make_pivot_view_dynamic'),
    ]

    operations = [

        migrations.RunPython(code=create_site, reverse_code=delete_site),

        migrations.RunSQL(
            f"""
                CREATE VIEW geo_tellus_point AS
                SELECT
                  tellus.objnr_leverancier as display,
                  cast('tellussen/tellus' as varchar(30)) as type,
                  tellus.standplaats,
                  site.domain || 'tellus/tellus/' || tellus.id || '/' AS uri,
                  tellus.geometrie AS geometrie
                FROM
                  tellus_data_tellus tellus , django_site site
                WHERE
                  tellus.geometrie IS NOT NULL and site.name = '{API_DOMAIN}';
            """)
    ]
