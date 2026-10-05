ARG BASE_IMAGE=registry.redhat.io/rhel9/python-312
FROM ${BASE_IMAGE}

# Exec form: the hardened image has no shell and no chown.
USER 0
RUN ["python3", "-m", "venv", "/opt/venv"]

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /opt/app
COPY requirements.txt .
RUN ["/opt/venv/bin/python3", "-m", "pip", "install", "--no-cache-dir", "-r", "requirements.txt"]
COPY app.py .
COPY static static/

USER ${CONTAINER_DEFAULT_USER:-1001}
EXPOSE 8080
CMD ["/opt/venv/bin/python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
