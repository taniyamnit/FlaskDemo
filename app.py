from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    name = 'JK International'
    return render_template('about.html', name = name)

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')




    
app.run(debug = True)


