FROM tiangolo/uvicorn-gunicorn:python3.7

RUN pip install --no-cache-dir fastapi

COPY ./requirements.txt /root
RUN pip install -r /root/requirements.txt

COPY ./app /app