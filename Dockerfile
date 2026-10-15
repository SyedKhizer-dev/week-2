FROM python:3.13-slim

WORKDIR /app

COPY app/ ./app/
COPY tests/ ./tests/

CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
