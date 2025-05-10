FROM python:3.12.5
Expose 80
ENV FLASK_app=app.py
WORKDIR /app
COPY ./app.py .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD gunicorn -w 4 -b :80 app:app