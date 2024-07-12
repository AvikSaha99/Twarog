from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from main import getPrediction
import os

UPLOAD_FOLDER = 'static/images/'
app = Flask(__name__, static_folder="static")
app.secret_key = "secret key"

#Define the upload folder to save images uploaded by the user. 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Define the route to be home. 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/basalcell')
def basalcell():
    return render_template('basalcell.html')

@app.route('/actinic')
def actinic():
    return render_template('actinic.html')

@app.route('/melanocytic')
def melanocytic():
    return render_template('melanocytic.html')

@app.route('/benign')
def benign():
    return render_template('benign.html')

@app.route('/melanoma')
def melanoma():
    return render_template('melanoma.html')

@app.route('/dermatofibroma')
def dermatofibroma():
    return render_template('dermatofibroma.html')

@app.route('/vascular')
def vascular():
    return render_template('vascular.html')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html')


#Add Post method to the decorator to allow for form submission. 
@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)  #Use this werkzeug method to secure filename. 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #getPrediction(filename)
            label = getPrediction(filename)
            flash(label)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash(full_filename)
            return redirect('/')


if __name__ == "__main__":
    app.run()