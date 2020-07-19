FROM python:3.7-slim


WORKDIR /app
COPY . /app
RUN apt-get update

RUN apt-get install -y python-opencv
RUN pip3 install -r requirements.txt 
EXPOSE 5001 
ENTRYPOINT [ "python3" ] 
CMD ["application.py" ] 

