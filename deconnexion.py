#!/usr/bin/python
# coding: utf-8
# Antonin Guyot

from mod_python import Session, util
import fonctions

def index(req):
	req.content_type = "text/html"
	sess=Session.Session(req)
	sess.delete()
	util.redirect(req, 'form-connexion.py')