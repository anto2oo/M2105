#!/bin/python
# Antonin Guyot
# coding: utf-8

from mod_python import Session
import fonctions

def index(req):
	req.content_type = "text/html"
	sess = Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)

	req.write(fonctions.codeHTML("Liste des contacts","""<b> Liste des contacts </b> <br/> Rechercher un nom : <input type="text" onkeyup="chargementContacts(this.value)"/> 
		<div id="liste"></div>""" + fonctions.lien("menu.py", "Retour au menu")) + """
<script>
function chargementContacts(value) {
  if(value == null){
  	value = "";
  }
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("liste").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "affiche-liste.py?nom=" + value, true);
  xhttp.send();
}
chargementContacts();
</script>""")