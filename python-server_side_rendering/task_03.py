from flask import Flask, render_template, request
import os
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
def items():
     # read the JSON file
    with open('items.json', 'r') as items_file:
        # Gets the dictionary with the list
        item_data = json.load(items_file)

    # item.data.get extracts the list and passes to template
    return render_template('items.html', items=item_data.get("items"))

@app.route('/products')
def products():
     
     # Check URL for query parameter 'source' (JSON or CSV) and store it
     source = request.args.get('source')
     
     # Optional unique id for specific product
     id_param = request.args.get('id', type=int)
     
     valid_sources = ['json', 'csv']
     
     # if source is not json or csv, return "wrong source"
     if not source or source not in valid_sources:
          return render_template('product_display.html', error="Wrong source")
    
    # if json, read and parse
     if source == 'json':
          with open('products.json', 'r', encoding='utf-8') as json_file:
               product_data = json.load(json_file)
               headers = list(product_data[0].keys())
               
    # if csv, read and parse
     if source == 'csv':
          with open('products.csv', 'r', encoding='utf-8') as csv_file:
               data = csv.DictReader(csv_file)
               headers = data.fieldnames
               product_data = list(data)
     
     # if product id is provided
     if id_param:
          filtered_products = []
         # if id provided - show product
          for product in product_data:
               if int(product['id']) == id_param:
                    filtered_products.append(product)

          # if id provided but not found, display "product not found"
          if not filtered_products:
               return render_template('product_display.html', error="Product not found")
     
     #if id not provided - display all
     else:
          filtered_products = product_data

     return render_template('product_display.html', headers=headers, products=filtered_products)

if __name__ == '__main__':
       app.run(debug=True, port=5000)