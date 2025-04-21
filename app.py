from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'simple_cart_secret'

# Dummy product list
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1000},
    {'id': 2, 'name': 'Headphones', 'price': 200},
    {'id': 3, 'name': 'Keyboard', 'price': 150},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    for product in products:
        if product['id'] == product_id:
            cart.append(product)
            break
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return "Thank you for your purchase!"

if __name__ == '__main__':
    app.run(debug=True)
