#!/bin/python
# coding: utf-8
# Antonin Guyot

import fonctions

def index(req):
	req.content_type = "text/html"
	req.write(fonctions.codeHTML("Mon premier script", "<i>Voici mon premier script de web dynamique!</i>"))