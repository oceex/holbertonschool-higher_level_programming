import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
    except Exception:
        data = {}
    return render_template('items.html', items=data.get("items", []))


JSON_FILE = 'products.json'
CSV_FILE = 'products.csv'


def read_json_data(filepath=JSON_FILE):
    with open(filepath, 'r') as f:
        data = json.load(f)
    # Normalize types so JSON and CSV output match
    for product in data:
        product['id'] = int(product['id'])
        product['price'] = float(product['price'])
    return data


def read_csv_data(filepath=CSV_FILE):
    products = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    if source == 'json':
        data = read_json_data()
    elif source == 'csv':
        data = read_csv_data()
    else:
        return render_template('product_display.html', error="Wrong source")
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Product not found")

        match = next((p for p in data if p['id'] == product_id), None)
        if match is None:
            return render_template('product_display.html', error="Product not found")
        data = [match]

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)