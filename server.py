from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'secret'  # set a secret key for security


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        fruit_count = int(
            request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
        order_details = {
            'products': {
                'sb': request.form['strawberry'],
                'rb': request.form['raspberry'],
                'ap': request.form['apple']
            },
            'f_name': request.form['first_name'],
            'l_name': request.form['last_name'],
            's_id': request.form['student_id'],
            'total_products': fruit_count,
            'order_date': datetime.today().strftime('%B %d' + ' at ' + ' %I:%M:%S %p')
        }
        # guardar en BBDD
        print("Hacer cargo de $100 en BBDD")
        session['order_details'] = order_details
        return redirect("/checkout")
    else:
        return render_template("checkout.html", order_details=session['order_details'])


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
