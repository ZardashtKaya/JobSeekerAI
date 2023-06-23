from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")

def index(name=None):
    url_for('static', filename='grayscale.js')
    return render_template("index.html",name=name)
if __name__ == "__main__":
    
    app.run(debug=True)

