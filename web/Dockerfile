FROM amsterdam/docker_python:latest
MAINTAINER datapunt@amsterdam.nl

ENV PYTHONUNBUFFERED 1
ENV CONSUL_HOST=${CONSUL_HOST:-notset}
ENV CONSUL_PORT=${CONSUL_PORT:-8500}
ENV DATAPUNT_API_URL=${DATAPUNT_API_URL:-https://api.data.amsterdam.nl/}
ARG TELLUS_OBJECTSTORE_PASSWORD
ENV TELLUS_OBJECTSTORE_PASSWORD=$TELLUS_OBJECTSTORE_PASSWORD

EXPOSE 8000

RUN apt-get install -y \
		gdal-bin \
		libgeos-dev \
		netcat \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& adduser --system datapunt \
	&& mkdir -p /static \
	&& chown datapunt /static \
	&& pip install uwsgi

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
USER datapunt

COPY tellus_app /app/
COPY .jenkins-import /.jenkins-import/

RUN export DJANGO_SETTINGS_MODULE=tellus.settings

CMD ["/app/docker-run.sh"]

