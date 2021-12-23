## HTTP METHODS
from flask import Flask, render_template,request 

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')

def hello(name=None):
    #return render_template('hello.html', name=name)
    #return render_template('hello.html', template_name=name)
    age = 22
    # return render_template('hello.html', template_name=name, template_age = age)
    #return render_template('hello.html', template_name=name, template_age = age, pet_list = pets, pet_names_dict = pet_names)
    #pets = ['cat', 'dog', 'bird', 'fish']
    #pet_names = {'cat' : 'cccc', 'dog' :'dddd'}

    return 'Hello'
if __name__ == '__main__':    
    app.run()
    
