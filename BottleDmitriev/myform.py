from datetime import datetime
import re
from bottle import post, request

@post('/home', method='post')
def my_form():
	quest = request.forms.get('QUEST')
	mail = request.forms.get('ADRESS')
	name = request.forms.get('NAME')
	error = ""

	if quest == "":
		error += "Question field was empty; "
	if mail == "":
		error += "Mail field was empty; "
	if name == "":
		error += "Name field was empty"
	if error != "":
		return error[0:len(error)-2] if error[-1] == " " else error
	
		

	if (re.fullmatch("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", mail)):
		return f"Thanks, {name}! The answer will be sent to the mail {mail} ; Access Date: {datetime.now().date()}"
	else:
		return "Your email  was invalid format"
