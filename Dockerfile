FROM python:3.11.7-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

# Install necessary packages before pip install pymssql
RUN apt-get update 
RUN apt-get install libraqm-dev -y
    
RUN pip install --upgrade pip

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt

COPY src src
COPY modules modules
COPY api api
COPY font font
COPY just_some_tools_cache just_some_tools_cache

EXPOSE 8086