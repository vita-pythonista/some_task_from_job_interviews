FROM python:3.9
WORKDIR /test
VOLUME /volume
COPY . /test
RUN pip install -r requirements.txt
CMD pytest -v test_filter.pyc