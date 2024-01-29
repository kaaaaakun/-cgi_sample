#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n\n")

print("<html><body>")
form = cgi.FieldStorage()

for key in form:
    value = form[key].value
    print('<p>%s: %s</p>' % (key, value))

print("</body></html>")

