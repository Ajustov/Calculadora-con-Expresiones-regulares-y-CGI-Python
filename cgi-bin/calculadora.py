
import cgi
import re
import math

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
expresion = form.getvalue("expresion", "")

print("<html><body>")
print("<h2>Resultado</h2>")

# Expresión regular permitida:
# números, operadores básicos, paréntesis, punto decimal
patron = r'^[0-9+\-*/(). ]+$'

if not re.match(patron, expresion):
    print("<p>Error: expresión no válida</p>")
else:
    try:
        # Reemplazos opcionales (extensión)
        expresion = expresion.replace("raiz", "math.sqrt")

        resultado = eval(expresion)

        print(f"<p>Expresión: {expresion}</p>")
        print(f"<p>Resultado: {resultado:.2f}</p>")
    except ZeroDivisionError:
        print("<p>Error: división por cero</p>")
    except Exception:
        print("<p>Error al evaluar la expresión</p>")

print('<a href="/html/index.html">Volver</a>')
print("</body></html>")
