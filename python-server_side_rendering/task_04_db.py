from flask import Flask, render_template, request
import  json, csv, sqlite3

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
    with open("items.json") as file:
        items = json.load(file)
    return render_template('items.html', items = items)

@app.route('/products')
def products():
    query = request.args.get('source')
    id = request.args.get('id', type=int)

    if not query:
        data = []
    elif query == "json":
        with open('products.json') as jf:
            data = json.load(jf)
    elif query == "csv":
        with open('products.csv') as cf:
            data = list(csv.DictReader(cf))
    elif query == "sql":
        db = sqlite3.connect('products.db')
        cursor = db.cursor()

        if id: 
            cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
        else:
            cursor.execute('SELECT * FROM products')
        
        product_data = cursor.fetchall()
        if not product_data:
            return render_template('product_display.html', error="Product not found")
        
        data = []
        for product in product_data:
                
            data.append(
                {
                    'id': product[0],
                    'name': product[1],
                    'category': product[2],
                    'price': product[3]
                }
            )   
        db.close()
    else:
        return render_template('product_display.html', error="Wrong source")

    if id:
        data = [item for item in data if int(item['id']) == id]

    return render_template('product_display.html', products = data), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)