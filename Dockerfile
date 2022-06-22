FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH = /opt/code/

RUN echo "Asia/Shanghai" > /etc/timezone \
  && apt-get update \
  && apt-get install -y python3-pip curl tzdata \
  && apt-get -y autoremove --purge \
  && apt-get -y clean && apt-get -y autoclean \
  && dpkg-reconfigure -f noninteractive tzdata

ADD ./ /opt/code/
RUN pip3 install -r /opt/code/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --extra-index-url https://pypi.python.org/simple --trusted-host mirrors.aliyun.com \
  && rm -rf /root/.cache && rm -rf /tmp/* && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/code/
CMD ["/usr/bin/python3", "main.py"]
