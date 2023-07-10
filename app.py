from flask import Flask, request,render_template, json
import pickle
import pandas as pd
import os
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/',methods=["Get","POST"])
def home():
    return render_template("index.html")

@app.route('/predict',methods=["Get","POST"])
def predict():
    new_file = request.files['file']
    target_path = os.path.join("upload",new_file.filename)
    new_file.save(target_path)

    image = cv2.imread(target_path, 0)
    image = data_validation(image)

    with open("ml/MLP.pkl", 'rb') as file:
            classifier = pickle.load(file)
    prediction = classifier.predict(image)

    clase_predicha = round(prediction.tolist()[0])

    # Imprimir el resultado de la predicción
    if clase_predicha == 0:
        return "La imagen fue clasificada como 'Glaucoma Negativo'."
    else:
        return "La imagen fue clasificada como 'Glaucoma Positivo'."


def data_validation(image):
    IMAGE_SIZE = (224,224)
    image = cv2.resize(image, IMAGE_SIZE)
    image = image.flatten()
    image = np.expand_dims(image, axis=0)
    return image

if __name__ == '__main__':
     app.run(debug=True, port=5002)
