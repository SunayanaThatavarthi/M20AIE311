FROM python:3.7.5-alpine
COPY . /application
WORKDIR /application
RUN pip install -r prerequisites.txt
ENTRYPOINT [ "python3" ]
CMD ["application.py"]
