import cv2
import sys
from tensorflow.keras.models import model_from_json

import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

json_file = open('/Users/tejas1.gaikwad/Downloads/model_1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("/Users/tejas1.gaikwad/Downloads/model_2.h5")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def pred():
    print("[INFO]: Loaded model from disk")
    
    class_names = ['T_shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    
    inp = "t.png"
    test_img = cv2.imread(inp, cv2.IMREAD_GRAYSCALE) 
    ret, test_img = cv2.threshold(test_img, 127, 255, cv2.THRESH_BINARY)
    test_img = cv2.resize(test_img,(28,28)).astype('float32')/255
    test_img = test_img.reshape(1,28,28,1)
    output = class_names[np.argmax(loaded_model.predict(test_img))]
    return render_template('index.html', prediction_text='Predicted Class is: {}'.format(output))

    
if __name__ == "__main__":
    print("[INFO]: Loaded model from disk:1")
    app.run(debug=True)