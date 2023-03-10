FROM --platform=linux/amd64 ubuntu:latest

COPY . /app

# switch working directory
WORKDIR /app
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
EXPOSE 5000

RUN pip install debugpy
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive
CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:5000", "app:app"]