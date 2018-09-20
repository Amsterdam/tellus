import os
import logging
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tellus.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.db import connection

INSERT_TELLUS_EXPANDED = """
TRUNCATE tellus_data_expanded CASCADE;
INSERT INTO tellus_data_expanded (
     id_tellus_data,
     tijd_van,
     tijd_tot,
     richting,
     validatie,
     representatief,
     meetraai,
     lengte_categorie_id,
     snelheids_categorie_id,
     id_tellus,
     meetwaarde,
     lengte_interval,
     snelheid_interval) 
    (SELECT 
        tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c1 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's1'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c2 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's2'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c3 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's3'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c4 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's4'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c5 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's5'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c6 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's6'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c7 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's7'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c8 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's8'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c9 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's9'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c10 AS meetwaarde,
        'l1'::text AS lengte_interval,
        's10'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c11 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's1'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c12 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's2'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c13 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's3'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c14 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's4'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c15 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's5'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c16 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's6'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c17 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's7'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c18 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's8'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c19 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's9'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c20 AS meetwaarde,
        'l2'::text AS lengte_interval,
        's10'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c21 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's1'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c22 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's2'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c23 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's3'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c24 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's4'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c25 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's5'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c26 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's6'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c27 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's7'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c28 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's8'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c29 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's9'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c30 AS meetwaarde,
        'l3'::text AS lengte_interval,
        's10'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c31 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's1'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c32 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's2'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c33 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's3'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c34 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's4'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c35 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's5'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c36 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's6'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c37 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's7'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c38 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's8'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c39 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's9'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c40 AS meetwaarde,
        'l4'::text AS lengte_interval,
        's10'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c41 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's1'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c42 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's2'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c43 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's3'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c44 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's4'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c45 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's5'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c46 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's6'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c47 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's7'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c48 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's8'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c49 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's9'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c50 AS meetwaarde,
        'l5'::text AS lengte_interval,
        's10'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c51 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's1'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c52 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's2'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c53 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's3'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c54 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's4'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c55 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's5'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c56 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's6'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c57 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's7'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c58 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's8'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c59 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's9'::text AS snelheid_interval
       FROM tellus_data_tellusdata
    UNION ALL
     SELECT tellus_data_tellusdata.id,
        tellus_data_tellusdata.tijd_van,
        tellus_data_tellusdata.tijd_tot,
        tellus_data_tellusdata.richting,
        tellus_data_tellusdata.validatie,
        tellus_data_tellusdata.representatief,
        tellus_data_tellusdata.meetraai,
        tellus_data_tellusdata.lengte_categorie_id,
        tellus_data_tellusdata.snelheids_categorie_id,
        tellus_data_tellusdata.tellus_id,
        tellus_data_tellusdata.c60 AS meetwaarde,
        'l6'::text AS lengte_interval,
        's10'::text AS snelheid_interval
       FROM tellus_data_tellusdata
      ORDER BY 1, 2, 3, 4, 12, 13);
    ALTER TABLE public.tellus_data_expanded
      OWNER TO tellus;
"""  # noqa

INSERT_TELLUS_RICHTING = """
    TRUNCATE tellus_data_tellus_richting CASCADE;
    INSERT INTO tellus_data_tellus_richting (richting, tellus_id, naam_richting)
        (SELECT
           unnest(array[id::TEXT || '-' ||'1',id::TEXT || '-' || '2']),
           id,
           -- unnest(array[1,2]) as id_richting,
           unnest(array[richting_1,richting_2])
        FROM
            public.tellus_data_tellus);
    """

INSERT_TELLUS_TOTAL_PER_HOUR_PER_DAY = """
    TRUNCATE public.tellus_data_cars_per_hour_per_day CASCADE;
    INSERT INTO public.tellus_data_cars_per_hour_per_day (
        tellus_id,
        richting_id,
        dag_uur_gemeten,
        dag_type,
        aantal)
        (SELECT
          id_tellus,
          id_tellus::TEXT || '-' || richting::TEXT,
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
        FROM tellus_data_expanded
        WHERE representatief = 1 AND validatie = 1
        GROUP BY
          id_tellus,
          richting,
          tijd_van
        ORDER BY
          id_tellus,
          richting,
          tijd_van);
    """


def logger():
    """
    Setup basic logging for console.
    Usage:
        Initialize the logger by adding the code at the top of your script:
        ``logger = logger()``
    TODO: add log file export
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S')
    logger = logging.getLogger(__name__)
    return logger


def sql_run(sql_query):
    """
    Simple sql runner.
    """
    with connection.cursor() as c:
        c.execute(sql_query)


def main():
    """
    Insert raw data into multiple api tables.
    """
    log = logger()
    log.info("started INSERT_TELLUS_EXPANDED")
    sql_run(INSERT_TELLUS_EXPANDED)
    log.info("started INSERT_TELLUS_RICHTING")
    sql_run(INSERT_TELLUS_RICHTING)
    log.info("started INSERT_TELLUS_TOTAL_PER_HOUR_PER_DAY")
    sql_run(INSERT_TELLUS_TOTAL_PER_HOUR_PER_DAY)
    log.info("All inserts finished.")


if __name__ == '__main__':
    main()
