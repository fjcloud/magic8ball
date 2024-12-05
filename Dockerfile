FROM registry.redhat.io/rhel9/python-312

USER 0
COPY app.py requirements.txt ./
COPY static static/
RUN chown -R 1001:0 ./
USER 1001

RUN pip install -r requirements.txt

EXPOSE 8080
CMD uvicorn app:app --host 0.0.0.0 --port 8080
