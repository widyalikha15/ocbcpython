#HTML Escaping
from flask import Flask

app = Flask(__name__)

#Routing
@app.route('/<page_name>')
def hello_world(page_name):
    html = 'Hello, World! <br/> <h1>Hello, World!</h1>'
    html += '<h2> This is {} page </h2>'.format(page_name)
    # html += f'<h2> This is {page_name} page </h2>'
    return html



