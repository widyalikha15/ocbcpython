# route/
# enspoint/   http
# url     	methods 	operation   	tujuannya (keterangan lebih jelasnya)
# ===============================================================
# /users  	+ GET       --> Read    	|| retrieve SEMUA daftar user yang tersedia di resource users tsb
# /users  	+ POST      --> Create      || buat data baru ke dalam resource tersebut
# /users/1	+ PUT       --> Update      || merubah data yang sudah exist di resource tsb, (data id nya sesuai yang disertakan)
# /users/1	+ DELETE    --> Delete   	|| menghapus data dari resource tsb (data id nya sesuai dengan yang disertakan)
# /users/1	+ GET       --> Read   		|| retrieve data yang diminta (data idnya sesuai dengan yang disertakan)


from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)