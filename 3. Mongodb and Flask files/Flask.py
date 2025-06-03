from flask import Flask, render_template_string, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.amazon_apan5400
product_collection = db.products



HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Product Information</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
        }

        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 600px;
            margin: 20px auto;
        }

        input[type="text"] {
            padding: 10px;
            margin-right: 10px;
            border-radius: 4px;
            border: 1px solid #ddd;
            width: calc(100% - 122px);
        }

        input[type="submit"] {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #66CDAA;
        }

        div {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 600px;
            margin: 20px auto;
        }

        h3 {
            color: #444;
        }

        p {
            color: #666;
        }
    </style>

</head>
<body>
    <form method="post">
        Parent ASIN: <input type="text" name="parent_asin" pattern="[A-Z0-9]{10}">
        <input type="submit" value="Search">
    </form>
    {% if product_info %}
    <div>
        <h3>Product Information</h3>
        <p>Parent ASIN: {{ product_info.parent_asin }}</p>
        <p>Title: {{ product_info.title }}</p>
        <p>Rating: {{ product_info.rating }}</p>
        <p>Average Rating: {{ product_info.average_rating }}</p>
        <p>Rating Number: {{ product_info.rating_number }}</p>
        <p>Price: ${{ product_info.price }}</p>
        <p>Store: {{ product_info.store }}</p>
        <p>Categories: {{ product_info.categories }}</p>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def search():
    product_info = None
    if request.method == 'POST':
        parent_asin = request.form.get('parent_asin')
        product_info = product_collection.find_one({"parent_asin": parent_asin})# Querying the database for product info based on 'parent_asin'
    return render_template_string(HTML_TEMPLATE, product_info=product_info)

if __name__ == '__main__':
    app.run(debug=True)
