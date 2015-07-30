import random 
import os 

from flask import (
	Flask,
	request, session,
	url_for, render_template, redirect
	)


#create a Flask application object
app= Flask( __name__)

#sesion variables are stored client-side(on the user´s browser)
#The content of this variables is encripted, so users cant actually
#read this contents, They could edit the session data,l but becouse it
#would not be "signed" with the secret key below, the server would
#reject is as invalid.
#You need the set secret key(random text) and keep it secret!
app.secret_key="muajajajajajaja"

#The pth to the directory containing our images.
#Wewill store a list of images file names in a session variable.
IMAGE_DIR= app.static_folder
##########################
### Helper functions #####
##########################

def init_game():
	#inialize a new deck (a list of file name)
	image_names= os.listdir(IMAGE_DIR)
	#shuffle the deck
	random.shuffle(image_names)
	#store it in the user´s sesion
	#"session" is a special global object that flask provides
	#Which exposes the basic session managment functionality
	session ["images"]= image_names


def select_from_deck():
	try:
		image_name=session["images"].pop()
	except IndexError:
		return None #sentinel
	return image_name



######################
#### View fuctions ###
######################

@app.route("/")
def index():
	init_game()
	return render_template("index.html")


@app.route("/draw")
def draw_card ():
	image_name= select_from_deck()
	if image_name is None:
		return render_template("gameover.html")
	return render_template("showcard.html", image_name=image_name)

if __name__ == '__main__':
	app.run(debug= True)



