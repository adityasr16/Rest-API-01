from flask import Flask, jsonify
app = Flask(__name__)

people_id = [{'name': 'Alice', 'birth-year': 1986},
          {'name': 'Bob', 'birth-year': 1985},
             {'name':'Aditya', 'birth_year':2000}]

@app.route("/")
def index():
    return "Hey Welcome!"

@app.route("/identity", methods=['GET'])
def get():

    return jsonify(people_id)


if __name__ == "__main__":

    app.run(debug=True)
