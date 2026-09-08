FROM python:3.8
WORKDIR /app
COPY . . 
RUN pip install -r requirements.txt    
ENV YOUR_NAME=Darren
EXPOSE 5500
ENTRYPOINT ["python","app.py"]