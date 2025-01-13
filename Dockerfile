FROM python:3.10.16-slim

WORKDIR /registry_factory

COPY ./registry_factory .
COPY ./requirements.txt .

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# ENTRYPOINT [ "python3", "-m", "gunicorn", "-b", "0.0.0.0:8002", "--workers", "2", "registry_factory.wsgi", "--reload" ]

ENTRYPOINT [ "/entrypoint.sh" ]
