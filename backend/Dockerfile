FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r reqs.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]