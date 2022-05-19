from flask import Flask

app = Flask(__name__)

@app.route('/')  #Decorator
def hello():
    return "<p><h4>Hello world from Flesk!!</h4><p/>"

@app.route('/second')
def second():
    return "<h1>Merhaba dünya</h1>"
    
@app.route("/third/subthird")
def third():
    return "<h2>This is a subpage</h2>"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'

if __name__ == '__main__':
    app.run(debug=True, port = 2000)
