# Flask-Number-Application
Basic containerized flask application to calculate odd, even, and prime numbers up to N.
Primes up to N may be calculated up to 25,000,000 currently.

Utilized Seive of Eratosthenes:  
   - https://primes.utm.edu/glossary/page.php?sort=SieveOfEratosthenes
   - https://www.ams.org/journals/bull/2013-50-02/S0273-0979-2012-01390-3/S0273-0979-2012-01390-3.pdf

Arguements:

http:[FLASK IP ADDRESS]/[PORT]/arguement/option
Arguement:
   - Arguements should be numbers 0<N<25,000,000.
Options:
-even,odd,prime

Dependencies:
   - Flask  (Any version)  
   - Python (3.x or higher)  
   - Docker (Most recent)
        
How to run the application locally:
- python numbersmart.py 

