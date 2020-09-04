# Flask-Number-Application
Basic containerized flask application to print odd, even, and prime numbers up to N.

How to run the application locally: (Assuming python and flask are both installed.)
- python numbersmart.py 

How to run the containerized version:

1) Start Docker app

2) Build docker image from the project source dir-(Execute): docker image build -t number-smart-app .


2) To view list of docker images- (Execute): docker image ls 

3) To run the containerized application- (Execute):docker run --name number-smart-flask-app -p 5000:5000 number-smart-flask-app

