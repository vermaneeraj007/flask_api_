from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/aboutus')
def aboutus():
    return "I AM I NEURON"

@app.route('/demo',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        operation = request.json ['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = 0
        if operation == "addition":
            result = num1 + num2
        elif operation == "subtraction":
            result = num1 - num2
        elif operation == "multiplication":
            result = num1 * num2
        else:
            result = num1/num2
            

        return "the operation is {} and the result is {}".format(operation,result)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0.", port=5001)