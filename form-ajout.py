#!/usr/bin/python
# coding: utf-8
# Antonin Guyot

from mod_python import Session
import psycopg2, fonctions

def index(req):
	req.content_type = "text/html"
	sess=Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)
	req.write(fonctions.codeHTML("Ajout d'un contact", """<b>Ajout d'un contact</b> <br/>
	<form action="ajout.py" method="post" name="form" onsubmit="return validate()">
	<table>
		<tr>
			<th></th>
			<th></th>
			<th></th>
		</tr>
		<tr>
			<td>
				<label for="nom">Nom</label>
			</td>
			<td>
				<input type="text" id="nom" name="nom" />
			</td>
			<td></td>
		</tr>
		<tr>
			<td>
				<label for="address">Adresse</label>
			</td>
			<td>
				<input type="address" id="address" name="address" />
			</td>
			<td>
			</td>
		</tr>
		<tr>
			<td>
				<label for="email">Mail</label>
			</td>
			<td>
				<input type="email" id="email" name="email" />
			</td>
			<td>
			</td>
		</tr>
		<tr>
			<td>
				<label for="telephone">Téléphone</label>
			</td>
			<td>
				<input type="telephone" id="telephone" name="telephone" />
			</td>
			<td>
				<input type="submit" value="Valider" />
			</td>
		</tr>
	</table>
</form>

<script>
function validate(){
	var nom = document.forms["form"]["nom"].value;
	if (nom == "") {
		alert("Le nom ne doit pas être vide !");
		return false;
	}

	var email = document.forms["form"]["email"].value;
	if(email.indexOf("@") == "-1"){
		alert("L'email doit contenir un @ !");
		return false;
	} else {
		var pos = email.indexOf("@")
	}
	if(email.indexOf(".", pos) == "-1"){
		alert("L'email doit contenir un . !");
		return false;
	}

	var address = document.forms["form"]["address"].value;
	if (address == "") {
		alert("L'adresse ne doit pas être vide !");
		return false;
	}

	var telephone = document.forms["form"]["telephone"].value;
	if(! /^\d+$/.test(telephone)){
		alert("Le numéro de téléphone doit être composé de chiffres");
		return false;
	}
	if(telephone.length != 10){
		alert("Le numéro de téléphone doit être une suite de 10 chiffres");
		return false;
	}
}
</script>
""" + fonctions.lien('menu.py','Retour au menu principal')))