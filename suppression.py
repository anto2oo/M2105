#!/usr/bin/python
# Antonin Guyot
# coding: utf-8

from mod_python import Session
import fonctions, psycopg2
from mod_python import util

def index(req):
	req.content_type = "text/html"
	sess=Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)
	_db=fonctions.connexionBD()
	_cursor=_db.cursor()
	_cursor.execute("DELETE FROM CONTACT WHERE id_util = %s AND id_contact = %s", (sess['id_util'], req.form["id_contact"],))
	if _cursor.rowcount == 0:
		req.write(fonctions.codeHTML("Erreur utilisateur", "Utilisateur introuvable. <br/> " + fonctions.lien('menu.py','Retour au menu principal')))
	else:
		_db.commit()
		util.redirect(req, 'liste.py')
	_db.close()