FROM python:3.8-slim-buster

#RUN cp /usr/share/zoneinfo/Asia/Baghdad /etc/localtime
#RUN echo "Asia/Baghdad" >  /etc/timezone
#RUN date
#RUN timedatectl

#Install dependencies:

RUN apt-get update
RUN apt-get upgrade -y

# Install Some usefull tools inside the container , it's optional
RUN apt-get install -y procps vi iproute2 curl

# To collect data and loging 
RUN pip3 install prometheus-client
# To expose API  
RUN pip3 install flask
# To generate fake data 
RUN pip3 install faker

# to track application and keep it started
RUN apt-get install supervisor -y

COPY supervisord.conf /etc/supervisor/supervisord.conf

ADD API.py /usr/bin/API.py
# This will watch the API.py and count 3 times failures then kill the container , to notice about something wrong going with that container
ADD kill.py /usr/bin/kill.py

#Set proper ownership and permissions
RUN chmod +x /usr/bin/kill.py
RUN chmod +x /usr/bin/API.py

CMD ["/usr/bin/supervisord"]


