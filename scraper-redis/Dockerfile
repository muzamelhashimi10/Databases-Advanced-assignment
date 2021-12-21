# Dockerfile, image, Container
FROM python:3.8

ADD main.py .

RUN pip install requests beautifulsoup4 redis

CMD ["python", "./main.py"]