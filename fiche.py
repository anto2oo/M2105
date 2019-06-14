#!/bin/python
# Antonin Guyot
# coding: utf-8

from mod_python import Session
import fonctions

def index(req):
	req.content_type = "text/html"
	sess = Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)

	_db = fonctions.connexionBD()
	_cursor = _db.cursor()
	_cursor.execute("SELECT * FROM CONTACT WHERE id_util = %s AND id_contact = %s", (sess['id_util'], req.form["id_contact"],))
	user = _cursor.fetchone()

	if user is None:
		req.write(fonctions.codeHTML("Erreur utilisateur", "Utilisateur introuvable. <br/> " + fonctions.lien('menu.py','Retour au menu principal')))
	else:
		table_contents = "<tr> <td>Nom</td> <td>" + user[1] + "</td></tr>"
		if user[2]:
			table_contents += "<tr> <td>Email</td> <td>" + fonctions.lien("mailto:" + user[2], user[2]) + "</td></tr>"
		if user[3]:
			table_contents += "<tr> <td>Téléphone</td> <td>" + user[3] + "</td></tr>"
		if user[4]:
			table_contents += "<tr> <td>Adresse</td> <td>" + user[4] + "</td></tr>"
		if user[5] != 0 and user[6] != 0:
			map_contents = """
			<link rel="stylesheet" href="leaflet.css" />
<div id="carte" style="width: 600px; height: 400px;">
</div>

<script src="leaflet.js"></script>
<script>
	var map = L.map("carte");
	map.setView({lat: """ + str(user[5]) + """, lon: """ + str(user[6]) + """}, 10);
	url = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png';
	var layer = L.tileLayer(url);
	layer.addTo(map);
	var m = L.marker ({lat: """ + str(user[5]) + """ ,  lon: """ + str(user[6]) + """});
	m.addTo(map);
</script>"""
		else:
			map_contents = "<p>Adresse du contact introuvable</p>"
		req.write(fonctions.codeHTML("Fiche d'un contact","""<b> Fiche d'un contact </b> <br/>
		<table>""" + table_contents + """</table>""" + map_contents + fonctions.lien("suppression.py?id_contact=" + str(user[0]) ,"Supprimer l'utilisateur") + "<br/>" + fonctions.lien("menu.py","Retour au menu principal")))

	_db.close()