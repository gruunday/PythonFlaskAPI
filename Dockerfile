FROM python:3.9

LABEL org.opencontainers.image.authors="gruunday@gmail.com"

ENV FLASK_APP app.py

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5005
WORKDIR src/
CMD ["gunicorn", "--config", "config/gunicorn-cfg.py", "app:app"]
