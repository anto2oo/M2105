#!/usr/bin/python
# coding: utf-8
# Antonin Guyot

from mod_python import Session
import fonctions, psycopg2, geocodage

def index(req):
	req.content_type = "text/html"
	sess=Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)
	_db=fonctions.connexionBD()
	_cursor=_db.cursor()

	_cursor.execute("INSERT INTO UTIL (login, mdp) VALUES (%s , %s)", (req.form['login'], req.form['password'],))
	_db.commit()

	req.write(fonctions.codeHTML("Menu principal","""
		<b> Nouvel utilisateur </b> <br/> 
		<p>""" + req.form['login'] + """ a bien été ajouté à la base de données. </p> 
		""" + fonctions.lien('menu.py','Retour au menu principal')))

	_db.close()
