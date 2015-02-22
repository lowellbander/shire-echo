from flask import Flask, render_template, request
import json
import requests
import os

general_webhook='https://hooks.slack.com/services/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'

government_webhook = "https://hooks.slack.com/services/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"

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
        r = requests.post(general_webhook, data=payload)
        return r.text
    else:
        print 'received GET'
        return 'you did a GET'

@app.route('/propose', methods=['GET', 'POST'])
def propose():
    if request.method == 'POST':
        proposition = request.form.get('text')
        user_name = request.form.get('user_name')
        payload = {'text': user_name + 
                " proposes the following legislation: \""
                + proposition + "\""}
        payload = json.dumps(payload)
        r = requests.post(government_webhook, data=payload)
        return r.text
    else:
        print 'received GET'
        return 'you did a GET'

if __name__ == '__main__':
    app.run()
