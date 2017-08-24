import os
from flask import Flask, request, render_template
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
 
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    upload_result = None
    thumbnail_url1 = None
    thumbnail_url2 = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            upload_result = upload(file, public_id = "sudip")
        return "ok"
    else:
        return render_template('upload_form.html')
 
if __name__ == "__main__":
    app.debug = True
    #tala ko line maile milcha ki bhanera try gareko tara kam garena 
    #ValueError: Must supply api_key bhancha
    #app.config['CLOUDINARY_URL'] = "cloudinary://418193537422982:ayEj_qE71n2sYdQWcgg3qi9YWjo@instantum"
    app.run()
