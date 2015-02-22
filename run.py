from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "hello world"

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        print request.data
        return request.data
    else:
        return 'you did a GET'

if __name__ == '__main__':
    app.run(debug=True)
