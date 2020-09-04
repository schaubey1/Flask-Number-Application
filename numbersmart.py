from flask import Flask
from flask import jsonify

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
        return jsonify([x for x in range(1, number + 1) if x % 2 == 0])
    else:
        return jsonify(boundsErr)


@app.route('/<int:number>/prime', methods=['GET'])
def displayPrime(number):
    primeList = []
    for i in range(2, number + 1):
        if i not in primeList:
            for j in range(i * i, number + 1, i):
                primeList.append(j)
    return jsonify(primeList)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=False)
