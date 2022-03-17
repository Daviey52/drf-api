# Django REST Framework & Docker

## Overview

Use Django REST Framework to create an API, then “containerize” it with Docker.

### Feature Tasks and Requirements

1. Rebuild a custom version of Things API demo project from scratch.
2. Replace things_project and Thing with your own application and model.
3. Your model must have at least as many fields as demo’s model.
4. Your model must have one field that is a foreign key to user.
NOTE: You are not required to build any templates for this lab.

### Features - Docker

1. NOTE Refer to the class demo for built out Dockerfile and docker-compose.yml examples.
2. Update Dockerfile and docker-compose.yml if needed.

### Stretch Goals

1. Research using a production server vs. the built in development server.
2. Research using postgres instead of sqlite as database.

### Implementation Notes

1. If you get an allowed host error examine the bug details and update code as needed.
2. When Docker installed and docker files are ready to go then run…
    $ docker-compose up
3. To shut docker down enter ctrl+c
4. You’ll learn a better way soon

### User Acceptance Tests

Modify provided unit tests in demo to work for your project.

### Configuration

Create a virtual environment inside drf-api.

Use the drf-api folder as the root of your project’s git repository.
