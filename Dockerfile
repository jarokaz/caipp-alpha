
FROM tensorflow/tensorflow:2.2.0rc2-py3
 
RUN pip install --upgrade pip
RUN pip install Flask==1.1.2
RUN pip install google-cloud-storage
 
COPY server.py /
 
ENV FLASK_APP=server.py
 
ENTRYPOINT ["flask", "run"]
