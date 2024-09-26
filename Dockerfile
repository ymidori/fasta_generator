FROM python:3.8.6-buster

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
ENV PATH $PATH:/root/.poetry/bin

# install dependencies
WORKDIR /tmp
COPY ./poetry.lock /tmp/
COPY ./pyproject.toml /tmp/
RUN poetry config virtualenvs.create false \
    && poetry install \
    && rm poetry.lock \
    && rm pyproject.toml

# editable installation
WORKDIR /opt/fasta_transfomer
COPY . /opt/fasta_transfomer
RUN poetry build \
    && tar -xvf dist/*.tar.gz --wildcards --no-anchored '*/setup.py' --strip=1 \
    && pip install -e . \
    && rm setup.py
