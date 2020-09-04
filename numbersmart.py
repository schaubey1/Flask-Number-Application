from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome! Use URL: http://127.0.0.1:5000/! Enter the url/int to see your number. '

@app.route('/<int:number>',methods=['GET'])		#display integer method
def displayIntegers(number):
	if number>0:
		output=list()
		i=1
		while i<number+1: 			#loop through and append numbers for printing.
			output.append(i)
			i+=1
		return jsonify(output)
	else: 
		return 'Please try again with a higher number.'

@app.route('/<int:number>/odd',methods=['GET'])
def displayOdd(number):					#display odds method
	print(number)
	output=list()
	if number>1:
		i=0					#loop through and append numbers for printing.
		while i<number+1:
			if i% 2 != 0:			#only add odd numbers to our list.
				output.append(i)
			i+=1
		return jsonify(output)
	else:
		return "You entered: 1. Please try a higher number."

@app.route('/<int:number>/even',methods=['GET'])
def displayEven(number):				#display even numbers method.
	if number>1:
		output=list()				#init list
		i=0					#init counter, start at 0 since 0 is even.
		while i<number+1:
			if i% 2 == 0:
				output.append(i)
			i+=1
	return jsonify(output)

@app.route('/<int:number>/prime',methods=['GET'])
def displayPrime(number):
	output=list()					#init list
	i=2						#2 is the first prime number, set our counter to this.
	if number>1:
		for x in range(i,number+1):		#loop through entire arange, set prime flag as true by default.
			prime=True			
			for i in range(2,x):		#Determine which numbers are not prime.
				if x%i==0:		#if cursor is divisble by number with no remainder, it is not prime.
					prime=False
			if prime==True:			#append and print
				output.append(x)
	else: 
		return 'Number too small.'
	return jsonify(output)

			

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = False)



