FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /app.

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

COPY ./advertisements .

RUN chmod +x ./entrypoint.sh

CMD ["./entrypoint.sh"]
