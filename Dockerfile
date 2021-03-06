
from alpine:latest

RUN apk add --no-cache python3-dev 

RUN apk add --no-cache py3-pip \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt                                                                            

EXPOSE 4000-8000

ENTRYPOINT  ["python3"]

CMD ["controller.py"]