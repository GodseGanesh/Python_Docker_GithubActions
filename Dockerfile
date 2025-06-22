FROM ubuntu

RUN  apt update
RUN  apt install -y  python3
RUN  apt install -y python3-pip

WORKDIR /app

COPY app/main.py .

EXPOSE 8000


ENTRYPOINT [ "python3" ,"main.py" ]