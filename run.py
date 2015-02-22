from flask import Flask, render_template, request
import json
import requests
import os

#WEBHOOK_URL = 'https://hooks.slack.com/services/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'

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "hello world"

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        text = request.form.get('text')
        payload = {'text': text}
        payload = json.dumps(payload)
        r = requests.post(os.environ['WEBHOOK_URL'], data=payload)
        return r.text
    else:
        print 'received GET'
        return 'you did a GET'

if __name__ == '__main__':
    app.run()
