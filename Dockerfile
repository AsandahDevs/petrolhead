FROM --platform=linux/amd64 python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR  /app/car_inventory

COPY requirements.txt requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "--pythonpath","/app/car_inventory", "car_inventory.wsgi:application"]