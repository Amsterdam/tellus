# -*- coding: utf-8 -*-
# Generated by Eelke on 2018-09-03 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tellus_data", "0017_table_tellus_expanded"),
    ]

    operations = [
        migrations.RunSQL("""
            DROP TABLE IF EXISTS public.tellus_data_cars_per_hour_per_day;
            CREATE TABLE public.tellus_data_cars_per_hour_per_day(
                id SERIAL PRIMARY KEY,
                id_tellus INT,
                id_richting TEXT,
                dag_uur_gemeten TIMESTAMP,
                dag_type TEXT,
                aantal INT);

            INSERT INTO public.tellus_data_cars_per_hour_per_day (
                id_tellus,
                id_richting,
                dag_uur_gemeten,
                dag_type,
                aantal)
                (SELECT
                  tellus_id,
                  tellus_id::TEXT || '-' || richting::TEXT,
                  tijd_van,
                  (CASE
                  WHEN
                    DATE_PART('day', tijd_van) NOT IN (0,6)
                  THEN 'Werkdag'
                  WHEN
                    DATE_PART('day', tijd_van) IN (0,6)
                  THEN
                    'Weekend'
                  END) AS dag_type,
                  sum(meetwaarde) as aantal
                FROM tellus_data_tellus_expanded
                WHERE representatief = 1 AND validatie = 1
                GROUP BY 
                  tellus_id,
                  richting,
                  tijd_van
                ORDER BY
                  tellus_id,
                  richting,
                  tijd_van);

            ALTER TABLE public.tellus_data_cars_per_hour_per_day
              OWNER TO tellus;
        """),
    ]