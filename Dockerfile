FROM tonghs/python:3.8-ubuntu

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/opt/code/

ADD ./ /opt/code/
RUN pip3 install -v -r /opt/code/requirements.txt -i http://mirrors.aliyun.com/pypi/simple --extra-index-url https://pypi.douban.com/simple --trusted-host mirrors.aliyun.com \
  && rm -rf /root/.cache && rm -rf /tmp/* && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/code/
CMD ["/usr/bin/python3", "main.py"]
