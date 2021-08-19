FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt app.py ./
RUN pip install --no-cache-dir -r requirements.txt && mkdir /usr/src/uploads

EXPOSE 5000

CMD [ "python", "./app.py" ]