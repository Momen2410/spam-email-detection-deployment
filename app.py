import flask

app = flask.Flask(__name__)

@app.route('/')
def welcome():
    return '<html><H1>Welcome for the first html code</H1></html>'

@app.route('/index')
def index():
    return '<html><H1>this second page</H1></html>'

if __name__ == '__main__':
    app.run(debug=True)