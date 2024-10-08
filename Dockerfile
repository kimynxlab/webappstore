FROM python:3.9-slim


#Install flask 
RUN pip install --upgrade pip && pip3 install flask mysql-connector-python 

# workdir 
WORKDIR /app

# Add ower application to the workdir 
COPY  application/* . 

# Configure the application 
ENV FLASK_APP=/app/webapp.py 

EXPOSE 5000 

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "-p", "5000"]
