#!/bin/python
# coding: utf-8

from mod_python import Session
import fonctions

def index(req):
	req.content_type = "text/html"
	sess = Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)

	_db = fonctions.connexionBD()
	_cursor = _db.cursor()
	_cursor.execute("SELECT longitude, latitude, nom, id_contact FROM CONTACT WHERE id_util = %s", (sess['id_util'],))
	markers = ""
	_db.close()

	req.write(fonctions.codeHTML("Localisation", """
<label for="search">Rechercher un contact :</label>
<input type="text" id="search" onkeyup="chargementMarqueurs(this.value)"/>
<br><br>
<link rel="stylesheet" href="leaflet.css" />
<div id="carte" style="width: 600px; height: 400px;">
</div>

<script src="leaflet.js"></script>
<script>
var map = L.map("carte");
url = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png';
var layer = L.tileLayer(url);
var layerGroup = L.layerGroup().addTo(map);
layer.addTo(map);

chargementMarqueurs();

function chargementMarqueurs(filter) {
  if(filter == null){
  	filter = "";
  }
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     eval(this.responseText);
    }
  };
  xhttp.open("GET", "affiche-markers.py?nom=" + filter, true);
  xhttp.send();
}
</script>
"""))