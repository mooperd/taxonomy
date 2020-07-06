import csv
from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/county/<search_term>')
def towns_in_county(search_term):
    return_list = []
    for row in data:
        if row["county"] == search_term:
            return_list.append(row)
    return jsonify(return_list)    




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