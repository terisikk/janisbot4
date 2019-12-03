FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY entrypoint.sh /
RUN chmod +x entrypoint.sh

ENV JANISBOT_CONFIG "\${GITHUB_WORKSPACE}/conf/default.conf"

ENTRYPOINT [ "/entrypoint.sh" ]
