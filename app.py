from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Replace 'Your Name' with your actual name
    name = 'Vivek Naina Prashant' 
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)