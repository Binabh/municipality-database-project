# Dockerfile

# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

# Set work directory
WORKDIR /code

# Copy project
COPY . /code/

# Install dependencies
RUN pip install -r requirements.txt
