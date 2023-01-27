Cloudflare Zero Trust Access Managed Network Server: Testing
============================================================
We test this server in our production environment and use it full time as part of our Zero Trust deployment.

Testing Requirements
--------------------
All code tested must follow these testing rules:

1. All code must be tested against a real Cloudflare ZTA environment.
2. Changes to code should be tested to avoid breaking existing infrastructure.
3. Code should pass `pre-commit` checks.

pre-commit
----------
This repo uses Yelp's [pre-commit](https://pre-commit.com/) to manage some pre-commit hooks automatically.  
In order to use the hooks, make sure you have `pre-commit`, and `pylint` in your `$PATH`.  
Once in your path you should run `pre-commit install` in order to configure it. If you push commits that fail pre-commit, your PR will
not be merged.

Local Docker
------------
You can run Docker using locally built containers via

    docker-compose up -d

poetry
------
This project uses [poetry](https://python-poetry.org/) for Python requirements
both for development and building the Docker container.

Python tests
------------
Coming soon ;)

Return to [README](README.md)
