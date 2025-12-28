#!/usr/bin/env python3

import cgi
import re

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
expresion = form.getfirst("expresion", "")

print("<html>")
print("<body>")
print("<h2>Resultado</h2>")

patron = r'^[0-9+\-*/(). ]+$'

if not re.match(patron, expresion):
    print("<p>Error: expresion no valida</p>")
else:
    try:
        resultado = eval(expresion)
        print("<p>Expresion: {}</p>".format(expresion))
        print("<p>Resultado: {:.2f}</p>".format(resultado))
    except ZeroDivisionError:
        print("<p>Error: division por cero</p>")
    except Exception:
        print("<p>Error al evaluar la expresion</p>")

print('<br><a href="/calculadora/html/index.html">Volver</a>')
print("</body>")
print("</html>")
