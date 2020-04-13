from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/enterprise')
def enterprise():
    return render_template('enterprise.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/sign-in')
def login():
    return render_template('login.html')


@app.route('/sign-up')
def register():
    return render_template('register.html')
    
@app.route('/start')
def start():
    return render_template('start.html')


if __name__ == '__main__':
    app.run(debug=True)



