from flask import Flask, request
from flask_cors import CORS, cross_origin
from PIL import Image, ImageOps
import numpy as np
import io

IMG_SIZE = 128

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["GET"])
@cross_origin()
def root():
    return {"message":"Up and running!"}

@app.route("/prepare", methods=["POST"])
@cross_origin()
def prepare():
    file = request.files['file']
    image = preprocessing(file.read())
    return {"image": image.tolist()}

def preprocessing(file_content):
    image = Image.open(io.BytesIO(file_content))
    image = ImageOps.grayscale(image)
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.asarray(image)

    return image
