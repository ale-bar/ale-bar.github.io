from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)

def read_csv():
    data = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@app.route('/')
def index():
    tableData = read_csv()
    return render_template('index.html', tableData=tableData)

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.json

    with open('data.csv', 'a', newline='') as csvfile:
        fieldnames = ['word1', 'word2', 'word3']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(data)

    return jsonify({'status': 'success'})

