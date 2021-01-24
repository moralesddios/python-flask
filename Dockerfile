FROM tiangolo/uwsgi-nginx-flask:python3.8
WORKDIR /app
COPY ./requirements.txt /app
COPY ./main.py /app
COPY ./app /app/app
RUN pip install -r requirements.txt