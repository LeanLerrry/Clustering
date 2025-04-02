FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

EXPOSE 10000

CMD ["gunicorn", "--config", "gunicorn.conf.py", "src.api:app"]