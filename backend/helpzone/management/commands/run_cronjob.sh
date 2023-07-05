#!/bin/bash
cd /usr/app/
python3 manage.py qtd_handle >> /var/log/cron.log 2>&1
