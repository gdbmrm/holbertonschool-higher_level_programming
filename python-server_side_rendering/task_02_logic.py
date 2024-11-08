from flask import Flask, render_template
import json

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
            items = data.get('items', [])
    except Exception as e:
        print(f"{e}")
        items = []
    return render_template('items.html', list_items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
