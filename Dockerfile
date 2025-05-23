FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

COPY templates/ templates/

EXPOSE 5000

CMD python app.py