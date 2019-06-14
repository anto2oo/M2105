#!/bin/python
# Antonin Guyot
# coding: utf-8

import fonctions

def index(req):
	req.content_type = "text/html"
	req.write(fonctions.codeHTML("Mon premier script", "<i>Voici mon premier script de web dynamique!</i>"))