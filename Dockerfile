FROM python:3.13.0rc3-slim-bullseye AS app

RUN mkdir /vampi

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential bash nano g++ \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean

ENV vulnerable=1
ENV tokentimetolive=6000

ARG FLASK_DEBUG="false"
ENV FLASK_DEBUG="${FLASK_DEBUG}"

COPY . /vampi
WORKDIR /vampi

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "gunicorn"]
CMD ["-c", "python:conf.gunicorn", "app:vuln_app"]
