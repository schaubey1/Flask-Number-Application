import time

from flask import Flask
from flask import jsonify

app = Flask(__name__)

bounds_err = "The number you entered is out of bounds."
welcome_msg = "Welcome! Enter the url/int to see your number."


@app.route('/')
def index():
    return jsonify(welcome_msg)


@app.route('/<int:number>', methods=['GET'])
def display_integers(number):
    if number > 0:
        return jsonify(result=list(range(1, number + 1)))
    else:
        return jsonify(bounds_err)


@app.route('/<int:number>/odd', methods=['GET'])
def display_odd(number):
    if number > 1:
        result = list(range(1, number + 1))
        result = result[0::2]
        return jsonify(result)
    else:
        return jsonify(bounds_err)


@app.route('/<int:number>/even', methods=['GET'])
def display_even(number):
    if number > 1:
        result = list(range(0, number + 1))
        result = result[0::2]
        return jsonify(result)
    else:
        return jsonify(bounds_err)


@app.route('/<int:number>/prime', methods=['GET'])
def display_prime(number):
    # Create a boolean array "prime[0..n]" and
    # # initialize all entries it as true. A value
    # # in prime[i] will finally be false if i is
    # # Not a prime, else true.
    if number <= 1:
        return jsonify(bounds_err)

    prime = [True] * int(number + 1)
    prime_index = 2
    t0 = time.time()
    while prime_index * prime_index <= number + 1:
        # If prime[primeIndex] is not changed, then it is
        # a prime
        if prime[prime_index]:
            # Update all multiples of prime index.
            for i in range(prime_index * prime_index, number + 1, prime_index):
                prime[i] = False
        prime_index += 1
    # add all prime numbers to the list to be printed
    prime_list = []
    for iterator in range(2, number + 1):
        if prime[iterator]:
            prime_list.append(str(iterator))
    t1 = time.time()
    print("Execution time:", t1 - t0)
    return jsonify(prime_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
