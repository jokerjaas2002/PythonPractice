from flask import Flask, request, jsonify

app = Flask(__name__)

# Funciones de la calculadora
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

# Endpoint para manejar las operaciones
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data['operation']
    num1 = float(data['num1'])
    num2 = float(data['num2'])

    try:
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
