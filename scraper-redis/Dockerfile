# Dockerfile, image, Container
FROM python:3.8

ADD main.py .

RUN pip install pymongo redis

CMD ["python", "./main.py"]