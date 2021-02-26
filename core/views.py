from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """
<html>
	<head>
	    <title>Cliente Recomendado</title>
	</head>

	<body style="background-color:#A9BCF5;">
        <div align="center"><img src="https://pure.ups.edu.ec/skin/footerIcon/"/></div>

        <br>
        <br>

        <div align="center">

        <h1> Ingrese su numero de cedula o su DNI
        <br>
        <input id="a" type="nombre"/>
        <br>
        <input type="button" value="Consultar">

        </div>
    

	</body>
</html>
    """

def home(request):
    return HttpResponse(html_base)
