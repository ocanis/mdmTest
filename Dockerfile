FROM python:3.7
WORKDIR /usr/src/app

COPY strings.txt .
COPY main.py .
COPY sparseArray.py .

ENTRYPOINT ["python", "./main.py"]