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
	geocode = geocodage.geocodage(req.form['address'])
	if geocode != None:
		lat = geocode[0]
		lon = geocode[1]
	else:
		lat = 0
		lon = 0
	_cursor.execute("INSERT INTO CONTACT (id_util, nom, email, tel, adresse, latitude, longitude) VALUES (%s , %s, %s, %s, %s, %s, %s)", (sess['id_util'],req.form['nom'], req.form['email'], req.form['telephone'], req.form['address'], lat, lon))
	_db.commit()

	req.write(fonctions.codeHTML("Menu principal","""
		<b> Nouveau contact </b> <br/> 
		<p>""" + req.form['nom'] + """ a bien été ajouté à vos contacts. </p> 
		""" + fonctions.lien('menu.py','Retour au menu principal')))

	_db.close()
