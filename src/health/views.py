import logging

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import connection

try:
    from django.apps import apps

    get_model = apps.get_model
except ImportError:
    from django.db.models.loading import get_model

from django.http import HttpResponse

try:
    model = get_model(settings.HEALTH_MODEL)
except Exception as e:
    raise ImproperlyConfigured(
        f"settings.HEALTH_MODEL doesn't resolve to a useable model {str(e)}"
    )


log = logging.getLogger(__name__)


def health(request):
    # check debug
    if settings.DEBUG:
        log.exception("Debug mode not allowed in production")
        return HttpResponse(
            "Debug mode not allowed in production",
            content_type="text/plain",
            status=500,
        )

    # check database
    try:
        with connection.cursor() as cursor:
            cursor.execute("select 1")
            assert cursor.fetchone()
    except Exception as e:
        log.exception(f"Database connectivity failed: {str(e)}")
        return HttpResponse(
            "Database connectivity failed", content_type="text/plain", status=500
        )

    return HttpResponse("Connectivity OK", content_type="text/plain", status=200)


def check_data(request):

    if model.objects.all().count() < 30000:
        return HttpResponse(
            "Too few tellus data in the database", content_type="text/plain", status=500
        )
    return HttpResponse("Database data OK", content_type="text/plain", status=200)
