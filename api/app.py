import flask
from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/api/<some_var>", methods=["GET"])
def hello(some_var):
    
    print('hello world',some_var)
    return flask.jsonify(ok=True)
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)