#!/bin/bash
service cron start
python3 manage.py qtd_handle
python3 manage.py runserver 0.0.0.0:8000