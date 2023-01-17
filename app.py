from flask import Flask, render_template, request, redirect
from yelp_login import yelp_login

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/results', methods=['POST'])
def results():
    email = request.form['email']
    password = request.form['password']
    # Grabs "email" and "password" input and runs yelp_login from yelp_login.py
    yelp_login(email, password)
    from yelp_login import listed_waits
    from yelp_login import restaurants
    return render_template('script_output.html', email=email, password=password, restaurants=restaurants, listed_waits=listed_waits)

if __name__ == '__main__':
    app.run(debug=True)



