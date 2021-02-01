FROM python:3

WORKDIR /usr/src/app

COPY ./run.py /usr/src/app/

EXPOSE 8080/tcp
EXPOSE 8081/tcp
EXPOSE 8082/tcp
EXPOSE 8083/tcp


CMD [ "python", "/usr/src/app/run.py" ]