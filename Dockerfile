FROM python:3
RUN pip3 install lxml
COPY ./* ./
CMD [ "python3", "robot.py" ]