FROM python:3.8.2-slim-buster

WORKDIR /usr/src/app
COPY requirements.txt app.py ./
RUN pip install --no-cache-dir -r requirements.txt && mkdir /usr/src/uploads

EXPOSE 8000

CMD [ "python", "./app.py" ]