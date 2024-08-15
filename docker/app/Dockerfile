FROM python:3.11 as base
LABEL maintainer = 'Samofalov Mihail <misasamofalov611@gmail.com>'
LABEL description = 'Docker image for the app'
LABEL version = '1.0'

FROM base as instal-poetry
ENV POETRY_VERSION=1.8.3
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_NO_INTERACTION=1
RUN pip install poetry==$POETRY_VERSION

FROM instal-poetry as install-dependencies-production
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

FROM install-dependencies-production as install_dependencies-dev
WORKDIR /app
RUN poetry install

FROM install_dependencies-dev as build
WORKDIR /app
COPY . .

FROM build as test
WORKDIR /app
CMD poetry run pytest

FROM build as production
WORKDIR /app
RUN rm -rf /app/tests
CMD poetry run gunicorn -b
