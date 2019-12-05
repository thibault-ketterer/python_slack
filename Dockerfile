FROM jfloff/alpine-python:latest-onbuild

COPY test_slack.py /tmp/test_slack.py

ENTRYPOINT ["python", "/tmp/test_slack.py"]
