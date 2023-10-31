

# ------------------------Chathini----------------------
from flask import Flask, flash, request, redirect, url_for, render_template
import pandas as pd
import pickle
import json

# ------------------------Chathini end----------------------

# ------------------------Kaveesha--------------------------

import pytesseract
from PIL import Image
import cv2

# ------------------------Kaveesha End----------------------


# ------------------------Image Upload----------------------
import urllib.request
import os
from werkzeug.utils import secure_filename

# ------------------------Image Upload----------------------


app = Flask(__name__)


# ------------------------Image Upload----------------------
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename("text.jpg")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


# ------------------------Image Upload  END----------------------

# ------------------------Foodprediction Chathini----------------------
@app.route('/foodcheck', methods=['GET', 'POST'])
def quzesselect():

    v1 = int(request.args.get('v1'))
    v2 = int(request.args.get('v2'))
    v3 = int(request.args.get('v3'))
    v4 = int(request.args.get('v4'))
    v5 = int(request.args.get('v5'))
    v6 = int(request.args.get('v6'))
    v7 = int(request.args.get('v7'))
    v8 = int(request.args.get('v8'))
    v9 = int(request.args.get('v9'))
    v10 = int(request.args.get('v10'))
    v11 = int(request.args.get('v11'))
  	

    df = pd.read_csv("fooddataset2.csv")
    df.head()

    inputs = df.drop('Suitability',axis='columns')
    target = df['Suitability']

    from sklearn.preprocessing import LabelEncoder

    # le_Height = LabelEncoder()
    # le_Weight = LabelEncoder()
    # le_Age = LabelEncoder()
    le_Diet = LabelEncoder()
    le_Allergies = LabelEncoder()
    le_Health = LabelEncoder()
    # le_FunctionTime = LabelEncoder()

    # inputs['Height_n'] = le_Height.fit_transform(inputs['Height'])
    # inputs['Weight_n'] = le_Weight.fit_transform(inputs['Weight'])
    # inputs['Age_n'] = le_Age.fit_transform(inputs['Age'])
    inputs['Gender_n'] = le_Diet.fit_transform(inputs['Diet'])
    inputs['FavoriteColor_n'] = le_Allergies.fit_transform(inputs['Allergies'])   # catogorical variable handling 
    inputs['FunctionType_n'] = le_Health.fit_transform(inputs['Health'])
    # inputs['FunctionTime_n'] = le_FunctionTime.fit_transform(inputs['FunctionTime'])
    inputs.head()

    inputs_n = inputs.drop(['Diet','Allergies','Health'],axis='columns')
    # inputs_n

    from sklearn import tree

    model = tree.DecisionTreeClassifier()

    model.fit(inputs_n,target) #train the model

    model.score(inputs_n, target)# test accuracy 

    output = model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11]]) #get prediction 
    # output = "test"
    # result = {"prediction": output.tolist()}
    # json_data = json.dumps(result)
    # return output
    # return 'Player Status: {}'.format(output)
    return (format(output))
    # return json_data
    # print(output)
    
# ------------------------Foodprediction Chathini----------------------

#--------------------------Item List Sacn Predict - Kaveesha  -----------------------------
@app.route('/ocr', methods=['GET'])
def ocr():
    # try:
        # Get the uploaded image from the request
        # image = request.files['image']
        print("hello this ")

        sub = "grttt"
        # Perform OCR using Tesseract
        print(Image.open("text2.jpg"))

        # myconfig = r"--psm 6 --oem 3"

        # myconfig = r'--oem 3 --psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        myconfig = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

        text = pytesseract.image_to_string(Image.open("static\\uploads\\text.jpg"), config=myconfig)
        
        print(text)

        # Return the extracted text as JSON
        # return jsonify({'text': text})
        return text
    # except Exception as e:
    #     return jsonify({'error': str(e)})
    
    #--------------------------Item List Sacn Predict - Kaveesha  END-----------------------------
  
if __name__ == '__main__':

  app.run(debug=True, port=5000)