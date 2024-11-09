#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

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
def item():
    try:
        with open("items.json", "r") as file_to_open:
            data = json.load(file_to_open)
            items = data.get("items")
    except Exception as e:
        print(f"{e}")
        items = []
    return render_template('items.html', items=items)


@app.route('/products', defaults={'id': None})
@app.route('/products/<id>')
def display_data(id=None):

    query = request.args.get('source')
    id = request.args.get('id')

    if query == "json":
        try:
            with open("products.json", "r") as json_file:
                json_response = json.load(json_file)
                if id:
                    for item in json_response:
                        if str(item.get('id')) == id:
                            return render_template(
                                'product_display.html', response=item)
                else:
                    return render_template(
                        'product_display.html', response="Product not found")

                return render_template(
                    'product_display.html', response=json_response)

        except FileNotFoundError:
            return render_template(
                "product_display.html", message="JSON file not found")

    elif query == "csv":
        try:
            with open("products.csv", "r") as csv_file:
                spamreader = csv.DictReader(csv_file, quotechar="|")
                csv_response = [row for row in spamreader]
                if id:
                    for row in csv_response:
                        if row.get("id") == id:
                            return render_template(
                                'product_display.html', response=row)

                return render_template(
                    'product_display.html', response=csv_response)

        except FileNotFoundError:
            return render_template(
                "product_display.html", message="JSON file not found")
    else:
        return render_template(
            "product_display.html", message="Wrong source")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
