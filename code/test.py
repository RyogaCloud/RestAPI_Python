from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello'

if __name__ == "__main__":
    app.run(host='localhost', port=3000, threaded=True)