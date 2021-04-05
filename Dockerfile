FROM ubuntu:18.04
MAINTAINER kaysilen "ohoh430@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3.7
RUN apt-get install -y python3-pip python-dev build-essential vim
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip3 install mahjong
ENTRYPOINT ["python3"]
CMD ["app.py"]