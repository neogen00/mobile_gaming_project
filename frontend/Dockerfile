FROM python:3.7

WORKDIR /usr/app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./ ./

ENV PYTHONPATH "${PYTHONPATH}:/usr/app"

CMD ["streamlit", "run", "index.py"]