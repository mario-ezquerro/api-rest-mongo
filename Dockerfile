From python:3.6

LABEL maintainer "mario.ezquerro@bosonit.com"
LABEL description "This is a docker to API to maker CRUD operations with mongo."
LABEL version "1.0"

ENV PROJECT_DIR=/usr/api
ENV HOST=0.0.0.0
ENV PORT=5000
WORKDIR $PROJECT_DIR 

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./config.py $PROJECT_DIR
COPY ./run-app.py $PROJECT_DIR
COPY ./app $PROJECT_DIR/app

EXPOSE $PORT
HEALTHCHECK CMD curl --fail http://$HOST:$PORT || exit 1

ENTRYPOINT ["python", "run-app.py"]
