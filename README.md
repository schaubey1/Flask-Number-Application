# Flask-Number-Application
Basic containerized flask application to calculate odd, even, and prime numbers up to N.

Utilized Seive of Eratosthenes:  
   - https://primes.utm.edu/glossary/page.php?sort=SieveOfEratosthenes
   - https://www.ams.org/journals/bull/2013-50-02/S0273-0979-2012-01390-3/S0273-0979-2012-01390-3.pdf



Dependencies:
   - Flask  (Any version)  
   - Python (3.x or higher)  
   - Docker (Most recent)
        
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

