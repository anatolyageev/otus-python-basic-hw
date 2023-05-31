# To run application in docker:
# docker build . -t app
# docker run -p XXXX:8000 -it app
# XXXX - put here your prefereble port

FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ping-pong ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000