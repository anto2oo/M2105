#!/bin/python
# coding: utf-8
# Antonin Guyot

from mod_python import Session
import fonctions

def index(req):
	req.content_type = "text/html"
	sess = Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)
	if sess['id_util'] == 1:
		create_util = "<li>" + fonctions.lien('form-ajout-util.py', 'Ajout d\'un utilisateur') + "</li>"
	else:
		create_util = ""

	req.write(fonctions.codeHTML("Menu principal","""<b> Menu principal </b> <br/> Vous êtes connecté en tant que <b> """ + sess['login'] + """. </b><ul>
	<li>"""+fonctions.lien('form-ajout.py', 'Ajout d\'un contact')+"""</li>
	<li>"""+fonctions.lien('liste.py', 'Liste de contacts')+"""</li>
	<li>"""+fonctions.lien('localisation.py', 'Carte des contacts')+"""</li>
	""" + create_util + """
	<li>"""+fonctions.lien('deconnexion.py', 'Déconnexion')+"""</li>
	</ul>
	
	"""))