FROM python:3.13-slim-bookworm

WORKDIR /app/src

RUN pip install poetry==2.1.4 &&  \
    poetry config virtualenvs.create false && \
    poetry config installer.max-workers 10

COPY . .

RUN poetry install --no-root

CMD ["python", "-m", "web"]