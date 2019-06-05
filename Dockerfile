FROM python:3.7-alpine

WORKDIR /src

ADD requirements.txt /src/

RUN pip install -r requirements.txt

ADD rest /src/rest/
ADD static /src/static/
ADD app.sh /src/

ENTRYPOINT ["sh", "app.sh"]