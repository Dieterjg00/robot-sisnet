FROM python:3
RUN pip3 install lxml
RUN pip3 install selenium
COPY ./* ./
CMD [ "python3", "robot.py" ]