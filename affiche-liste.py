#!/usr/bin/python
# coding: utf-8

from mod_python import Session
import fonctions, psycopg2

def index(req):
	req.content_type = "text/html"
	sess = Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)
	
	try:
		req.form["nom"]
	except KeyError:
		req.form["nom"] = ""

	_db = fonctions.connexionBD()
	_cursor = _db.cursor()
	_cursor.execute("SELECT * FROM CONTACT WHERE id_util = %s AND nom LIKE %s", (sess['id_util'], "%%" + req.form["nom"] + "%%",))
	_rows = _cursor.fetchall()

	req.write("<ul>")
	for row in _rows:
		req.write("<li>" + fonctions.lien("fiche.py?id_contact=" + str(row[0]), row[1]) + "</li>")
	req.write("</ul>")
	_db.close()
