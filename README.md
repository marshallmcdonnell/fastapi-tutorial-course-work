# FastAPI tutorial

This is my work going through [Learning FastAPI: The hard way](https://www.fastapitutorial.com/blog/fastapi-course/).

Differences from the main tutorial are:
  - I am using [poetry](https://python-poetry.org/) for package and dependency management


# Quickstart

Install (after git clone):
```
cd backend/
poetry install
```

Run:
```
poetry run uvicorn main:app
```

Then, navigate to backend app at:
```
http://localhost:8000
```

And OpenAPI docs at:
```
http://localhost:8000/docs
```

