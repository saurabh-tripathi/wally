FROM python:3.9

ENV POETRY_VERSION=1.1.5
ENV POETRY_HOME=/opt/poetry
ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN curl -sOSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py && \
    python get-poetry.py --yes && \
    rm get-poetry.py
RUN poetry config virtualenvs.create false

WORKDIR /godaddy-example
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-interaction

COPY . /wally
