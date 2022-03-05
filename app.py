import cv2
from tensorflow.keras.models import model_from_json

import numpy as np
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app,prefix='/api/v1')
auth = HTTPBasicAuth()

#this would be coming from tinydb Database, the format is of tinyDB database
USER_DATA = {
    "admin":"1234@1234"
    }


json_file = open('model_1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_2.h5")
class_names = ['T_shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# =============================================================================
# @auth.verify_password
# def verify (username,password):
#     if not (username and password):
#         return False
#     return USER_DATA.get(username)==password
# 
# class PrivateResource(Resource):
#     @auth.login_required
#     def get(self):
#         return {"meaning of life":42}
# =============================================================================

@app.route('/')
def home():
    #return("Welcome")
    return render_template('index.html')


@app.route('/predict_img',methods=['POST'])
def pred_img():
    
        
    print("[INFO]: Loaded model from disk")
    inp = "t.png"
    test_img = cv2.imread(inp, cv2.IMREAD_GRAYSCALE) 
    ret, test_img = cv2.threshold(test_img, 127, 255, cv2.THRESH_BINARY)
    test_img = cv2.resize(test_img,(28,28)).astype('float32')/255
    test_img = test_img.reshape(1,28,28,1)
    output = class_names[np.argmax(loaded_model.predict(test_img))]
    #return("Output is :"+output)
    return render_template('index.html', prediction_text='Predicted Class is: {}'.format(output))


@app.route('/predict_file',methods=['POST'])
def pred_file():
    print("[INFO]: Loaded model from disk 2")
    print(type(request.files.get("file")))
    
    test_img = cv2.imread("{}".format(request.files.get("file")), cv2.IMREAD_GRAYSCALE) 
    test_img = cv2.threshold(test_img, 127, 255, cv2.THRESH_BINARY)
    test_img = cv2.resize(test_img,(28,28),interpolation = cv2.INTER_AREA)
    test_img = test_img.reshape(1,28,28,1)
    output = class_names[np.argmax(loaded_model.predict(test_img))]
    return("Output is :"+output)
    #return render_template('index.html', prediction_text='Predicted Class is: {}'.format(output))

    
if __name__ == "__main__":
    print("[INFO]: Loaded model from disk:1")
    app.run(port=9082,debug=True)
    #app.run('0.0.0.0',port=9081,debug=True)
