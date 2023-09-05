FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip -r requirements.txt

CMD ["pytest", "tests/"]
