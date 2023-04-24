from datetime import datetime
import re
import pdb
import json
import os
from bottle import post, request, template



def regular_expr(mail):
    return re.fullmatch("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", mail)

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
	if len(quest) <= 3:
		return(template("index.tpl", year = datetime.now().year, error = "Your question is too short (must be at least 4 symbols)!"))
	if (quest.isnumeric()):
		return(template("index.tpl", year = datetime.now().year, error = "Your question cant be a number"))
	if (not regular_expr(mail)):
		return(template("index.tpl", year = datetime.now().year, error = "Your email  was invalid format")) #проверки
		
	jsonoutput = {}
	with open('data.txt') as infile:
		if not (os.stat("data.txt").st_size == 0):
			jsonoutput = json.load(infile)

			
	if (mail in jsonoutput.keys()):
		if (quest in jsonoutput[mail]):
			return(template("index.tpl", year = datetime.now().year, error = "Your have already asked this question"))
		jsonoutput[mail][0] = name
		jsonoutput[mail].append(quest)
	else:
		jsonoutput[mail] = [name, quest]

	with open('data.txt', 'w') as outfile:
		json.dump(jsonoutput, outfile, indent = 4)
		
	return f"Thanks, {name}! The answer will be sent to the mail {mail} ; Access Date: {datetime.now().date()}"
