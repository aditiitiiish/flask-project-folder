from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return render_template('index.html', success=True)
    return render_template('index.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
