# Python REST API template project

This is a template to implement a RESTful API using Python.  
It is based on [Flask](https://palletsprojects.com/p/flask/) framework.
There is one resource, called "resource" and supporting four verbs: GET, POST, PUT and DELETE.
The template features also a [Docker](https://www.docker.com/) image in order to deploy the API in a container.

[Here](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask) you can find a good tutorial on how to implement REST API in Python with Flask.

## Use

The root route provides this documentation:

    GET {{url}}/

Then we have the route to access the "resource" resource:

    GET {{url}}/resource/{{resource-id}}

    POST {{url}}/resource
    body:
    {
        "field": "resource-field"
    }

    PUT {{url}}/resource/{{resource-id}}
    body:
    {
        "field": "resource-field-modification"
    }

    DELETE {{url}}/resource/{{resource-id}}
    body:
    {
        "field": "resource-field-modification"
    }

## Deploy

### Install dependencies

    pip install -r requirements.txt

### Run unit test

    python src/test.py

### Run server

    python src/server.py

### Build Docker image

    docker image build -t rest-api-template .

### Run Docker container

    docker container run -p 5000:5000 -d rest-api-template
