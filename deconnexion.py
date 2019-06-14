#!/usr/bin/python
# Antonin Guyot
# coding: utf-8

from mod_python import Session, util
import fonctions

def index(req):
	req.content_type = "text/html"
	sess=Session.Session(req)
	sess.delete()
	util.redirect(req, 'form-connexion.py')