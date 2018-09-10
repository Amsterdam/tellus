# -*- coding: utf-8 -*-
# Generated by Eelke on 2018-09-03 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tellus_data", "0014_auto_20180903_1653"),
    ]

    operations = [
        migrations.RunSQL("""
            -- View: public.tellus_data_tellus_expanded

            DROP VIEW IF EXISTS public.tellus_data_tellus_expanded;

            CREATE VIEW public.tellus_data_tellus_expanded AS
             SELECT tdtdes.id,
                tdtdes.tijd_van,
                tdtdes.tijd_tot,
                tdtdes.richting,
                    CASE
                        WHEN tdtdes.richting = 1 THEN tdt.richting_1
                        WHEN tdtdes.richting = 2 THEN tdt.richting_2
                        ELSE 'nvt'::character varying
                    END AS richting_label,
                tdtdes.validatie,
                tdvc.label AS validatie_label,
                tdtdes.representatief,
                tdrc.label AS representatief_label,
                tdtdes.meetraai,
                tdmc.label AS meetraai_label,
                tdtdes.lengte_categorie_id,
                    CASE
                        WHEN tdtdes.lengte_interval = 'l1'::text THEN tdlc.l1
                        WHEN tdtdes.lengte_interval = 'l2'::text THEN tdlc.l2
                        WHEN tdtdes.lengte_interval = 'l3'::text THEN tdlc.l3
                        WHEN tdtdes.lengte_interval = 'l4'::text THEN tdlc.l4
                        WHEN tdtdes.lengte_interval = 'l5'::text THEN tdlc.l5
                        WHEN tdtdes.lengte_interval = 'l6'::text THEN tdlc.l6
                        ELSE 'nvt'::character varying
                    END AS lengte_label,
                tdtdes.snelheids_categorie_id,
                tdtdes.meetwaarde,
                tdtdes.lengte_interval,
                tdtdes.snelheid_interval,
                    CASE
                        WHEN tdtdes.snelheid_interval = 's1'::text THEN tdsc.s1
                        WHEN tdtdes.snelheid_interval = 's2'::text THEN tdsc.s2
                        WHEN tdtdes.snelheid_interval = 's3'::text THEN tdsc.s3
                        WHEN tdtdes.snelheid_interval = 's4'::text THEN tdsc.s4
                        WHEN tdtdes.snelheid_interval = 's5'::text THEN tdsc.s5
                        WHEN tdtdes.snelheid_interval = 's6'::text THEN tdsc.s6
                        WHEN tdtdes.snelheid_interval = 's7'::text THEN tdsc.s7
                        WHEN tdtdes.snelheid_interval = 's8'::text THEN tdsc.s8
                        WHEN tdtdes.snelheid_interval = 's9'::text THEN tdsc.s9
                        WHEN tdtdes.snelheid_interval = 's10'::text THEN tdsc.s10
                        ELSE 'nvt'::character varying
                    END AS snelheid_label,
                tdtdes.tellus_id,
                tdt.objnr_vor,
                tdt.objnr_leverancier,
                tdt.standplaats,
                tdt.zijstraat_a,
                tdt.zijstraat_b,
                tdt.richting_1,
                tdt.richting_2,
                tdt.latitude,
                tdt.longitude,
                tdt.snelheids_klasse_id
               FROM tellus_data_tellus_expanded_source tdtdes,
                tellus_data_tellus tdt,
                tellus_data_validatiecategorie tdvc,
                tellus_data_representatiefcategorie tdrc,
                tellus_data_meetraaicategorie tdmc,
                tellus_data_snelheidscategorie tdsc,
                tellus_data_lengtecategorie tdlc
              WHERE
                tdtdes.tellus_id = tdt.id AND
                tdtdes.validatie = tdvc.validatie AND
                tdtdes.representatief = tdrc.representatief AND
                tdtdes.meetraai = tdmc.meetraai AND
                tdtdes.snelheids_categorie_id = tdsc.klasse AND
                tdlc.klasse = 1
              ORDER BY
                tdtdes.id,
                tdtdes.tijd_van,
                tdtdes.tijd_tot,
                tdtdes.richting,
                tdtdes.lengte_interval,
                tdtdes.snelheid_interval;

            ALTER TABLE public.tellus_data_tellus_expanded
              OWNER TO tellus;

        """),
    ]
