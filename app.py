from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = False
    if request.method == 'POST':
        _ = request.form.get('player')
        result = True
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
