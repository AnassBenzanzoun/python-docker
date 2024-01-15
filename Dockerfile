FROM python:3.8-slim-buster
WORKDIR /app
ADD . /app
EXPOSE 80
CMD ["python", "main.py"]