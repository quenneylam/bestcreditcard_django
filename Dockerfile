FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY ./app/requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/
