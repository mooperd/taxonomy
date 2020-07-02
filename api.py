import csv
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root_data():
    data_to_be_serialised = [
    {"name": "Maddy", "status": "Confused"},
    {"name": "Danny", "status": "Evil"},
    {"name": "Andrew", "status": "Hungover"},
    {"name": "Mibéka", "status": "Lucid"}
        ]
    return jsonify(data_to_be_serialised)

if __name__ == '__main__':
    app.run(debug=True)