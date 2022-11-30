FROM python
WORKDIR /code
RUN pip install flask
RUN pip install mysql-connector-python
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# ENV PYTHONUNBUFFERED 1
COPY /python ./
CMD ["flask", "run"]
