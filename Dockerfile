FROM ubuntu:latest
COPY . /usr/app
EXPOSE 6050
WORKDIR /usr/app
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip install opencv-python-headless
RUN pip3 install -r /usr/app/requirements.txt
CMD python3 app.py

