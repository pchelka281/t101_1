FROM python:3.7-slim-buster
RUN mkdir ./code
COPY ./code ./code
WORKDIR ./code
CMD ["python", "./main.py"]
