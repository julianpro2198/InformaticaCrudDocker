FROM python:alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]