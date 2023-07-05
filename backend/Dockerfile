FROM ubuntu:20.04

RUN apt-get update && apt-get -y install cron
RUN apt-get -y install python3-pip

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/app/requirements.txt
RUN pip3 install -r requirements.txt

COPY helpzone/management/commands/qtd_handle.py /usr/app/helpzone/management/commands/qtd_handle.py
COPY helpzone/management/commands/my-cron /etc/cron.d/my-cron
COPY helpzone/management/commands/run_cronjob.sh /usr/app/run_cronjob.sh

RUN chmod 0644 /etc/cron.d/my-cron
RUN chmod +x /usr/app/run_cronjob.sh
RUN crontab /etc/cron.d/my-cron

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
