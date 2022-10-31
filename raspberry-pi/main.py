from flask import Flask, render_template, Response, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)