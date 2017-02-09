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
        ('tellus_data', '0007_geoview_tellus'),
    ]

    operations = [

        migrations.RunPython(code=create_site, reverse_code=delete_site),

    ]
