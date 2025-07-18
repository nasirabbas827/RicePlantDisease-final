from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

model = load_model('rice_disease_cnn_model.h5')
class_indices = {0: 'Bacterialblight', 1: 'Brownspot', 2: 'Leafsmut'}

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', error="No file selected")

        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', error="Empty file name")

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        img = preprocess_image(file_path)
        prediction = model.predict(img)
        class_idx = np.argmax(prediction)
        result = class_indices[class_idx]

        return render_template('index.html', result=result, img_path=file_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
