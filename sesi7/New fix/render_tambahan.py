## HTTP METHODS
from flask import Flask, render_template,request 

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')

def hello(name=None):
    
    age = 22
    #return render_template('hello.html', template_name=name, template_age = age)
    return 'Hello Render Template'
    
if __name__ == '__main__':    
    #app.run()
    app.run(debug=True)
