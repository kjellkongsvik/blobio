FROM python:3.6
RUN pip install pipenv
WORKDIR /src
COPY Pipfile* ./
RUN pipenv install --dev --system
ADD . .

RUN flake8
RUN isort -c
RUN black --check .

ENTRYPOINT [ "pytest" ]
