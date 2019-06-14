#!/bin/python
# Antonin Guyot
# coding: utf-8

from mod_python import Session
import fonctions, json

def index(req):
	req.content_type = "application/json"
	 
	_db = fonctions.connexionBD()
	_cursor = _db.cursor()
	_cursor.execute("SELECT * FROM Util WHERE login='{}'".format(req.form["login"]))
	if _cursor.fetchone() is not None:
		req.write(json.dumps({"taken": True}))
	else:
		req.write(json.dumps({"taken": False}))