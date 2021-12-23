from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#Routing

@app.route('/')
@app.route('/shop')
@app.route('/shoes')
@app.route('/food')

def hello_world():    
    return 'Hello, World!, </br> <h1> Hello, World! </h1>'

@app.route('/hello')
def hello():    
    return 'Hello, World!, </br> <h1> This is hello home! </h1>'


if __name__ == '__main__':    
    app.run()




