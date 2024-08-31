FROM python


USER webappuser 

#Install flask 
RUN pip3 install flask 

# workdir 
RUN mkdir /app 
WORKDIR /app

# Add ower application to the workdir 
ADD webapp.py . 

# Configure the application 
ENV expose FLASK_APP=/app/webapp.py 

EXPOSE 5000 

ENTRYPOINT ["flask","run","--host 0.0.0.0"]
