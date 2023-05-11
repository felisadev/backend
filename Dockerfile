FROM python:3.9-alpine

EXPOSE 8000

RUN apk update
RUN apk add --no-cache gcc python3-dev musl-dev libpq postgresql-dev

ADD . /

WORKDIR /

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
