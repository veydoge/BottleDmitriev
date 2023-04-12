from datetime import datetime
import re
import pdb
from bottle import post, request, template

@post('/home', method='post')
def my_form():
	quest = request.forms.get('QUEST')
	mail = request.forms.get('ADRESS')
	name = request.forms.get('NAME')
	error = ""
	questions = {}



	if quest == "":
		error += "Question field was empty; "
	if mail == "":
		error += "Mail field was empty; "
	if name == "":
		error += "Name field was empty"
	if error != "":
		return template("index.tpl", year = datetime.now().year, error = error[0:len(error)-2]) if error[-1] == " " else (template("index.tpl", year = datetime.now().year, error = error))
	
		

	if (re.fullmatch("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", mail)):
		questions[mail] = [name, quest]
		pdb.set_trace()
		return f"Thanks, {name}! The answer will be sent to the mail {mail} ; Access Date: {datetime.now().date()}"
	else:
		return(template("index.tpl", year = datetime.now().year, error = "Your email  was invalid format"))

