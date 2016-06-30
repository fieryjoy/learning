FROM ojajoh/docker-python3-oracle-base
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -U pip 
RUN pip3 install -r requirements.txt
ADD . /code/
