FROM python:alpine

WORKDIR /registry_factory

COPY ./registry_factory .
COPY ./requirements.txt .

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "-m", "gunicorn", "-b", "0.0.0.0:8000", "--workers", "2", "registry_factory.wsgi", "--reload" ]
