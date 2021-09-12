FROM python:3.9

RUN apt-get update

RUN pip install --user pipenv

ENV PYTHONPATH=/usr/src/app/
ENV PATH="$PATH:/root/.local/bin" \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.6

WORKDIR /usr/src/app

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml /usr/src/app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /usr/src/app/

CMD ["python", "main.py"]
