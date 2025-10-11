from Flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome To My Flask App Home Page!"
# A new route to the 'greet page' of our website
@app.route('/greet/<name>')
def greetpage(name):
    return render_template('greet.html', name=name)

if __name__ == '__main__':
   app.run(debug=True)