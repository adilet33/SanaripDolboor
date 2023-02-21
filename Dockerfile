FROM python:3.10


ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]