#!/usr/bin/python
# Antonin Guyot
# coding: utf-8

from mod_python import Session
import fonctions, psycopg2

def index(req):
	req.content_type = "text/javascript"
	sess = Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)
	
	try:
		req.form["nom"]
	except KeyError:
		req.form["nom"] = ""

	_db = fonctions.connexionBD()
	_cursor = _db.cursor()
	_cursor.execute("SELECT * FROM CONTACT WHERE id_util = %s AND nom LIKE %s", (sess['id_util'], "%%" + req.form["nom"] + "%%"))
	_rows = _cursor.fetchall()
	req.write("layerGroup.clearLayers();")
	bounds = ""
	for row in _rows:
		if row[5] != 0 and row[6] != 0:
			req.write("\nvar m = L.marker ({lat: " + str(row[5]) + " ,  lon: " + str(row[6]) + "});" )
			req.write("\nm.addTo(layerGroup); \nm.bindPopup('" + fonctions.lien("fiche.py?id_contact=" + str(row[0]), row[1]) + "');")
			bounds += "[" + str(row[5]) + ", " + str(row[6]) + "], "
	if bounds != "":
		req.write("\nmap.fitBounds([" + bounds + "]);")
	_db.close()