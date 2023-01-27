#
# Copyright 2023, Route 1337 LLC, All Rights Reserved.
#
# Maintainers:
# - Matthew Ahrenstein: @ahrenstein
#
# See LICENSE
#

FROM python:3.10
LABEL maintainer = "Route 1337 LLC <@route1337>"

# Copy the source code and poetry config to /app
COPY ./SourceCode/ /app
COPY pyproject.toml /app/

# Install some required packages
RUN apt-get update && apt-get install -y openssl
RUN mkdir /cert

# Configure the Python environment using poetry
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root

# Make sure logging to stdout works
ENV PYTHONUNBUFFERED=0

# Run the Flask server
CMD ["python", "-u", "/app/server.py"]
