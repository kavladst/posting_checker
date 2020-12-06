FROM python:3.9.0-buster

WORKDIR /opt/app
ENV PYTHONPATH=/opt/app:${PYTHONPATH}

COPY ./core ./core
COPY ./requirements.txt ./requirements.txt
RUN python -m pip install -r requirements.txt --no-cache-dir

COPY ./core ./core
COPY ./main.py .

EXPOSE 8000/tcp

CMD ["python", "main.py"]
