FROM python:3.10-slim

WORKDIR /app

COPY ./app /app
COPY ./model /model

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
