FROM ubuntu:20.04

ADD ./ /opt/code/

ENV DEBIAN_FRONTEND=noninteractive
RUN echo "Asia/Shanghai" > /etc/timezone \
  && apt-get update \
  && apt-get install -y python3 python3-dev python3-pip curl tzdata \
  && apt-get -y autoremove --purge \
  && apt-get -y clean && apt-get -y autoclean \
  && dpkg-reconfigure -f noninteractive tzdata \
  && pip3 install -r /opt/code/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --extra-index-url https://pypi.python.org/simple --trusted-host mirrors.aliyun.com \
  && rm -rf /root/.cache && rm -rf /tmp/* && rm /opt/code/docker-comp*.yml

ENV PYTHONPATH = /opt/code/
WORKDIR /opt/code/

CMD ["/usr/bin/python3", "main.py"]
