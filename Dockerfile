FROM python:3

WORKDIR my-vol2

copy test.py .

CMD ["python","test.py"]

