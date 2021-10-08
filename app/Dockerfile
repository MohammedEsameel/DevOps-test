FROM python:3.8-slim-buster

#RUN cp /usr/share/zoneinfo/Asia/Baghdad /etc/localtime
#RUN echo "Asia/Baghdad" >  /etc/timezone
#RUN date
#RUN timedatectl

#Install dependencies:

RUN apt-get update
RUN apt-get upgrade -y
RUN pip3 install prometheus-client 
RUN pip3 install flask 
RUN pip3 install faker

RUN apt-get install supervisor -y
COPY supervisord.conf /etc/supervisor/supervisord.conf

ADD API.py /usr/bin/API.py
ADD kill.py /usr/bin/kill.py

#Set proper ownership and permissions
RUN chmod +x /usr/bin/kill.py
RUN chmod +x /usr/bin/API.py

CMD ["/usr/bin/supervisord"]


