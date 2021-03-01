FROM python:3.7-alpine

RUN apk update \
    && apk add gcc python3-dev musl-dev curl \
    && apk add vim postgresql-dev 

WORKDIR /usr/app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY ./ ./

ENV PYTHONPATH "${PYTHONPATH}:/usr/app"

CMD ["flask", "run", "--host=0.0.0.0",  "--port=80"]