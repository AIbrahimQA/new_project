FROM python:3.6.9
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT /usr/local/bin/gunicorn --bind=0.0.0.0:5000 --workers=4 application:app
#ENTRYPOINT ["/usr/local/bin/python", "app.py"]
COPY . .
