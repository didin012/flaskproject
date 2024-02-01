FROM python:3.6.1-alpine
WORKDIR /flaskblog
ADD . /flaskblog

RUN pip install --upgrade pip
RUN pip install flask

CMD ["python","flaskblog.py"]