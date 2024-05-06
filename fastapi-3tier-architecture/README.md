# fastapi-3tier-architecture

This repository provides an approach on how to effectively structure a FastAPI application
with multiple services using 3-tier design pattern, integrate it with Postgres backend,
and implement straightforward OAuth2 Password authentication flow using Bearer and
JSON Web Tokens (JWT).

## How to install

Clone this repository and install using `pip`.

```bash
$ pip install --editable .
```

## How to run

Configure the relevant DSN string to your Postgres backend database in `.env` file,
or provide it from the environment variable `MYAPI_DATABASE__DSN`.

To run the application use following.

```bash
$ uvicorn app.main:app
```

or

```bash
$ MYAPI_DATABASE__DSN=postgresql://... uvicorn app.main:app
```
