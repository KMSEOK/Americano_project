FROM python:3.9

WORKDIR /code

COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .


