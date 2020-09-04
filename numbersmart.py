from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def index():

	return 'Welcome! Use URL: http://127.0.0.1:5000/! Enter the url/int to see your number. '

@app.route('/<int:number>',methods=['GET'])
def displayIntegers(number):
	if number>0:
		output=list()
		i=1
		while i<number+1:
			output.append(i)
			i+=1
		return jsonify(output)
	else: 
		return 'Please try again with a higher number.'

@app.route('/<int:number>/odd',methods=['GET'])
def displayOdd(number):
	print(number)
	output=list()
	if number>1:
		i=0
		while i<number+1:
			if i% 2 != 0:
				output.append(i)
			i+=1
		return jsonify(output)
	else:
		return "You entered: 1. Please try a higher number."
@app.route('/<int:number>/even',methods=['GET'])
def displayEven(number):
	if number>1:
		output=list()
		i=0
		while i<number+1:
			if i% 2 == 0:
				output.append(i)
			i+=1
	return jsonify(output)
@app.route('/<int:number>/prime',methods=['GET'])
def displayPrime(number):
	output=list()
	i=2
	if number>1:
		for x in range(i,number+1):
			prime=True
			for i in range(2,x):
				if x%i==0:
					prime=False
			if prime==True:
				output.append(x)
	else: 
		return 'Number too small.'
	return jsonify(output)

			

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = False)



