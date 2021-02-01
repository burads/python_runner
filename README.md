# python_runner
Simple python runner dockerfile that allows for python scripts to be run adhoc in a docker container

Dockerfile creates a simple python3 container that only adds a runner.
Dockerfile is writen to expose ports 8080 - 8083

Runner takes the following environment variables:
Environemnt Variable | Description
------------ | ------------
"PYTHON_WORKDIR" | the working directory mounted in the container
"PYTHON_REQUIREMENTS_FILE" | (optional) a python requirements file with packages to install using pip install -f
"PYTHON_FILE" | Defines the python file to run

example installs the flask packages and then starts a simple flask server. The server serves the time on 0.0.0.0:8080/time.

example can be started using the command:
```
docker run -it --rm -p 8080:8080 -v $(pwd)/example:/example -e PYTHON_WORKDIR=/example -e PYTHON_REQUIREMENTS_FILE=pipRequirements.txt -e PYTHON_FILE=webTime.py simonstiil/python_runner:latest
```