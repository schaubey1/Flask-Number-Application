from flask import Flask
from flask import jsonify
import time
app = Flask(__name__)

boundsErr = "The number you entered is out of bounds."
welcomeMsg = "Welcome! Enter the url/int to see your number."


@app.route('/')
def index():
    return jsonify(welcomeMsg)


@app.route('/<int:number>', methods=['GET'])
def displayIntegers(number):
    if number > 0:
        return jsonify([x for x in range(1, number + 1)])
    else:
        return jsonify(boundsErr)


@app.route('/<int:number>/odd', methods=['GET'])
def displayOdd(number):
    if number > 1:
        return jsonify([x for x in range(1, number + 1) if x % 2 != 0])
    else:
        return jsonify(boundsErr)


@app.route('/<int:number>/even', methods=['GET'])
def displayEven(number):
    if number > 1:
        return jsonify([x for x in range(0, number + 1) if x % 2 == 0])
    else:
        return jsonify(boundsErr)


@app.route('/<int:number>/prime', methods=['GET'])
def displayPrime(number):
    # Create a boolean array "prime[0..n]" and
    # # initialize all entries it as true. A value
    # # in prime[i] will finally be false if i is
    # # Not a prime, else true.
    intVal = int(number)
    prime = [True for i in range(intVal + 1)]
    primeIndex = 2
    t0 = time.time()
    while (primeIndex * primeIndex <= intVal):
        # If prime[primeIndex] is not changed, then it is
        # a prime
        if (prime[primeIndex]):
            # Update all multiples of prime index.
            for i in range(primeIndex * primeIndex, intVal + 1, primeIndex):
                prime[i] = False
        primeIndex += 1
    # add all prime numbers to the list to be printed
    primeList = []
    for index in range(2, intVal):
        if prime[index]:
            primeList.append(str(index))
    t1 = time.time()
    print("Execution time:", t1-t0)
    return jsonify(primeList)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8004, debug=False)
