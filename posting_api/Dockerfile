FROM python:3.9.0-buster

WORKDIR /opt/app
ENV PYTHONPATH=/opt/app:${PYTHONPATH}

COPY ./requirements ./requirements
RUN python -m pip install -r requirements/common.txt --no-cache-dir

COPY ./api ./api
COPY ./core ./core
COPY ./db ./db
COPY ./models ./models
COPY ./services ./services
COPY ./tests ./tests
COPY ./utils ./utils
COPY ./main.py .

EXPOSE 8000/tcp

CMD ["python", "main.py"]
