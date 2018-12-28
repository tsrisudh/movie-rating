FROM python:2.7-slim

RUN pip install requests

COPY movie.py /opt/odb.py

ENTRYPOINT ["python", "/opt/odb.py"]

