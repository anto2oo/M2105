#!/usr/bin/python
# coding: utf-8

from mod_python import Session
import psycopg2, fonctions

def index(req):
	req.content_type = "text/html"
	sess=Session.Session(req)
	fonctions.redirectionSiNonConnecte(req, sess)
	fonctions.redirectionSiNonRoot(req, sess)

	req.write(fonctions.codeHTML("Ajout d'un utilisateur", """<b>Ajout d'un utilisateur</b> <br/>
	<form action="ajout-util.py" method="post" name="form" onsubmit="return validate()">
	<table>
		<tr>
			<th></th>
			<th></th>
			<th></th>
		</tr>
		<tr>
			<td>
				<label for="login">Login</label>
			</td>
			<td>
				<input type="text" id="login" name="login" onblur="checkLogin(this.value)"/>
			</td>
			<td></td>
		</tr>
		<tr>
			<td>
				<label for="password">Mot de passe</label>
			</td>
			<td>
				<input type="password" id="password" name="password" />
			</td>
			<td>
			</td>
		</tr>
		<tr>
			<td>
				<label for="password-again">Confirmation du mot de passe</label>
			</td>
			<td>
				<input type="password" id="password-again" name="password-again" />
			</td>
			<td>
				<input type="submit" value="Valider" />
			</td>
		</tr>
	</table>
</form>

<script>
function validate(){
	var login = document.forms["form"]["login"].value;
	if (login == "") {
		alert("Le login ne doit pas être vide !");
		return false;
	}

	var password = document.forms["form"]["password"].value;
	if (password.length < 8) {
		alert("Le mot de passe doit faire plus de 8 caractères");
		return false;
	}

	var password_again = document.forms["form"]["password-again"].value;
	if (password != password_again) {
		alert("Les mots de passe ne correspondent pas");
		return false;
	}

	var login = document.forms["form"]["login"];
	if(login.getAttribute("available") == "no"){
		alert("Nom d'utilisateur déjà existant");
		return false;
	}
}

function checkLogin(login){
	var xhttp = new XMLHttpRequest();

	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			response = JSON.parse(this.responseText);
			if(response.taken){
				document.forms["form"]["login"].setAttribute("available", "no");
			} else {
				document.forms["form"]["login"].setAttribute("available", "yes");
			}
		}
	};

	xhttp.open("GET", "verif-util.py?login=" + login, true);
	xhttp.send();
}
</script>
""" + fonctions.lien('menu.py','Retour au menu principal')))