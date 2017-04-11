from django.conf import settings
from django.db import migrations

API_DOMAIN = 'API Domain'


class Migration(migrations.Migration):
    dependencies = [
        ('tellus_data', '0006_make_pivot_view_dynamic'),
    ]

    operations = [
        migrations.RunSQL(
            f"""
                CREATE VIEW geo_tellus_point AS
                SELECT
                  tellus.objnr_leverancier as display,
                  cast('tellussen/tellus' as varchar(30)) as type,
                  tellus.standplaats,
                  '{settings.DATAPUNT_API_URL}' || 'tellus/tellus/' || tellus.id || '/' AS uri,
                  tellus.geometrie AS geometrie
                FROM
                  tellus_data_tellus tellus
            """)
    ]
