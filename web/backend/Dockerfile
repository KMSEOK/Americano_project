FROM python:3.9

WORKDIR /code

COPY requirements.txt ./

RUN apt update && \
    apt install -y postgresql-client

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

