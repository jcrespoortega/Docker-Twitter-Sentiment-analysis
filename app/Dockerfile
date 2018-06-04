# our base image
FROM cloudera/quickstart:latest

RUN yum install -y python-pip 

# install Python modules needed by the Python app
# copy files required for the app to run
COPY requirements.txt /usr/src/app/

RUN pip install -r /usr/src/app/requirements.txt

COPY files/* /usr/src/app/files/

# run the application
CMD ["sh", "/usr/src/app/files/aplication.sh"]

