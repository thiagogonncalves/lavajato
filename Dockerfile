FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /app
WORKDIR /app
RUN apt update && apt-get upgrade -y
RUN apt install libsasl2-dev python-dev-is-python3 libldap2-dev libssl-dev gcc -y
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --upgrade
RUN python manage.py collectstatic --noinput
EXPOSE 8000