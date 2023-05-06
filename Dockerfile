FROM python:3.9-slim

# install needed packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql \
    gcc \
    libcairo2-dev \
    libpq-dev

# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD python manage.py migrate && gunicorn configurations.wsgi