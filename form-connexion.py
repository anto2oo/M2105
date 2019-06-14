#!/bin/python
# Antonin Guyot
# coding: utf-8

import fonctions

def index(req):
	req.content_type="text/html"
	req.write(fonctions.codeHTML("Formulaire de connexion", """<form action="connexion.py" method="post">
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
				<input type="text" id="login" name="login" />
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
				<input type="submit" value="Valider" />
			</td>
		</tr>
	</table>
</form>
"""))