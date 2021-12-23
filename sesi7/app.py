##
""" from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/shop')
@app.route('/shoes')

def hello_world():    
    return 'Hello, World! <br> <h1>WIDYA</h1>'

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == '__main__':   
    app.run() """

##
""" from flask import Flask

app = Flask(__name__)

# @app.route('/shoes')
# @app.route('/food')
# @app.route('/shop')
@app.route('/<page_name>')
def hello_world(page_name):
    html = 'Hello, World! <br/> <h1>Hello, World!</h1>'
    html += '<h2> This is {} page </h2>'.format(page_name)
    # html += f'<h2> This is {page_name} page </h2>'
    return html
 """

##
""" from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
#show he user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

if __name__ == '__main__':
    app.run() """

##
