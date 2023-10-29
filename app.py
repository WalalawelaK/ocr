from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
# import cv2
# from ocr_core import ocr_core

app = Flask(__name__)

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

        text = pytesseract.image_to_string(Image.open("text3.jpeg"), config=myconfig)
        
        print(text)

        # Return the extracted text as JSON
        # return jsonify({'text': text})
        return text
    # except Exception as e:
    #     return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()