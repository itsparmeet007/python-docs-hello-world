# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello I am Parmeet Singh 😁😉!!"


from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Python Calculator</h2>
    <form method="get" action="/calc">
      <input name="a" type="number" required>
      <input name="b" type="number" required>
      <select name="op">
        <option value="add">+</option>
        <option value="sub">-</option>
        <option value="mul">*</option>
        <option value="div">/</option>
      </select>
      <button type="submit">Calculate</button>
    </form>
    """

@app.route("/calc")
def calc():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    op = request.args.get("op")

    if op == "add":
        res = a + b
    elif op == "sub":
        res = a - b
    elif op == "mul":
        res = a * b
    elif op == "div":
        res = "Infinity" if b == 0 else a / b
    else:
        res = "Invalid operation"

    return f"<h3>Result: {res}</h3><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run()
