FROM python:3.10-slim-buster

LABEL "author"="Abraham Sanchez"

RUN apt update && \
    apt install --no-install-recommends -y \
    ffmpeg \
    && apt clean \
    && apt autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -U -q --no-cache-dir \
    pip \
    wheel

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ADD app/ app/

EXPOSE 8080

CMD ["hypercorn", "app.main:app", "--bind", "0.0.0.0:8080", "--access-logfile", "-"]
