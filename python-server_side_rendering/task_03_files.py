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


@app.route('/products', methods=['GET'])
def display_data():

    query = request.args.get('source')
    id = request.args.get('id', None)
    error_message = ""
    product = []

    try:
        if query == "json":
            with open("products.json", "r") as json_file:
                product = json.load(json_file)

        elif query == "csv":
            with open("products.csv", "r") as csv_file:
                spamreader = csv.DictReader(csv_file)
                product = [row for row in spamreader]
        else:
            error_message = "Wrong source"
        if id:
            product = [
                product for product in product
                if str(
                    product['id']) == id]

            if not product:
                error_message = "Product not found"

    except FileNotFoundError:
        error_message = "File not found"

    except json.JSONDecodeError:
        error_message = "Error decoding JSON file"

    except csv.Error:
        error_message = "Error reading CSV file"

    except Exception as e:
        error_message = f"Unexpected error: {e}"

    return render_template(
        "product_display.html",
        product=product,
        error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
