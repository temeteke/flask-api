FROM python:3.10-alpine

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN pip install gunicorn
COPY app.py ./
CMD ["gunicorn", "-b", "0.0.0.0:80", "--access-logfile", "-", "app:app"]

EXPOSE 80