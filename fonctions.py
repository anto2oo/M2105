#!/bin/python
# Antonin Guyot
# coding: utf-8

import psycopg2
from mod_python import util

def codeHTML(title, text):
	return("""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>""" + title  + """</title>
</head>

<body> """ + text + """</body>

</html>""")

def connexionBD():
	return(psycopg2.connect(host="localhost", dbname="devweb", user="devweb", password="123456"))

def lien(url, text):
	return("<a href=\"" + url + "\">" + text + "</a>")

def redirectionSiNonConnecte(req, sess):
	if(sess.is_new()):
		util.redirect(req, 'form-connexion.py')

def redirectionSiNonRoot(req, sess):
	if(sess['id_util'] != 1):
		util.redirect(req, 'form-connexion.py')
