from flask import render_template, Flask

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    #return 'Hello, World! <br/> <h1></h1>'
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()