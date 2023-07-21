FROM python:3.9

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /code

COPY ./poetry.lock /code/poetry.lock
COPY ./pyproject.toml /code/pyproject.toml
COPY ./.env /code/.env
COPY ./main.py /code/main.py
COPY ./app /code/app
COPY ./oracle /code/oracle

COPY ./certs/localhost.crt /etc/ssl/certs/
COPY ./certs/localhost.key /etc/ssl/certs/

RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt-get update && apt-get install -y alien libaio1 libaio-dev rlwrap
RUN mkdir -p /opt/oracle
RUN unzip /code/oracle/instantclient-11.2.0.4.0-linux.x64-basic.zip -d /opt/oracle
RUN unzip /code/oracle/instantclient-11.2.0.4.0-linux.x64-sdk.zip -d /opt/oracle
RUN unzip /code/oracle/instantclient-11.2.0.4.0-linux.x64-sqlplus.zip -d /opt/oracle
RUN ln -s /opt/oracle/instantclient_11_2/libclntsh.so.11.1 /usr/lib/libclntsh.so.11.1
RUN ln -s /opt/oracle/instantclient_11_2/libclntsh.so /usr/lib/libclntsh.so
RUN ln -s /opt/oracle/instantclient_11_2/libocci.so.11.1 /usr/lib/libocci.so.11.1
RUN ln -s /opt/oracle/instantclient_11_2/libocci.so /usr/lib/libocci.so
RUN ln -s /opt/oracle/instantclient_11_2/sqlplus /usr/local/bin/sqlplus
RUN ldconfig

ENV ORACLE_HOME=/opt/oracle/instantclient_11_2
ENV LD_LIBRARY_PATH=$ORACLE_HOME:$LD_LIBRARY_PATH

HEALTHCHECK --interval=30s --timeout=10s CMD curl -f http://localhost:8000/docs || exit 1

CMD ["python", "main.py"]