# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:53:46 2021

@author: Ajmal.VA
"""

from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

dic = {1 : 'Truck', 0 : 'Ship'}

model = load_model('model.h5')

model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(32,32))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 32,32,3)
	p = model.predict_classes(i)
	return dic[p[0]]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "A binary image classifier to accept user input as image and predict wheather it's a mango or jackfruit. Created and collaborated by Ajmal.Va, Alvin Antony Ms, Ancy Paul for the TinkerHub Build From Home Event."

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
