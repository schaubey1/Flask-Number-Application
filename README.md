# Flask-Number-Application
Basic containerized flask application to print odd, even, and prime numbers up to N.
Dependencies:
    Flask
    Python
How to run the application locally:
- python numbersmart.py 

How to run the containerized version:

1) Start Docker app

2) Build docker image from the project source dir:
docker image build -t number-smart-app .


2) To view list of docker images: 
docker image ls 

3) To run the containerized application:
docker run --name number-smart-flask-app -p 5000:5000 number-smart-flask-app

