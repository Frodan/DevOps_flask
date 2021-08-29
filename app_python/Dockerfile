FROM python:3.8.2-slim-buster

RUN adduser --disabled-password app --shell /bin/sh --home /home/app --quiet

WORKDIR /usr/src/app_python


COPY requirements.txt main.py __init__.py ./
COPY test ./test

USER app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python",  "-m", "test.test_main"]
#CMD [ "python", "./main.py" ]