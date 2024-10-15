from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    test()
    return "Hello, Flask!"

def test():
    num1 = 10
    num2 = 20
    sum = num1 + num2
    print(f"Sum: {sum}")

    multiplied = num1 * num2
    print(f"Product: {multiplied}")

if __name__ == '__main__':
    app.run(debug=True)
