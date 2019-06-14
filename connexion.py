#!/usr/bin/python
# coding: utf-8
# Antonin Guyot

from mod_python import Session
import fonctions

_db = fonctions.connexionBD()
_cursor = _db.cursor()

def index(req):
	req.content_type="text/html"
	_cursor.execute("SELECT mdp, id_util FROM UTIL WHERE login = %s", (req.form['login'],))
	query = _cursor.fetchone()
	if(query == None or req.form["password"] != query[0]):
		req.write(fonctions.codeHTML("Erreur", "Login ou mot de passe incorrects. " + fonctions.lien("form-connexion.py", "Connexion")))
	else:
		sess = Session.Session(req)
		sess["id_util"] = query[1]
		sess["login"] = req.form['login']
		sess.save()
		req.write(fonctions.codeHTML("Connexion réussie", fonctions.lien("menu.py", "Connexion réussie, allez au menu")))