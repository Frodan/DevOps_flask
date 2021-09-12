FROM python:3.8.2-slim-buster

RUN adduser --disabled-password app --shell /bin/sh --home /usr/src/app_python --quiet

WORKDIR /usr/src/app_python

COPY requirements.txt main.py __init__.py ./

USER app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python", "./main.py" ]