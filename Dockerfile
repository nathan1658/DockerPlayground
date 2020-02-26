FROM python:3

VOLUME ["/my-vol"]

WORKDIR my-vol

copy test.py .

CMD ["python","test.py"]

