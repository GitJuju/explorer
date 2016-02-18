#!/usr/bin/env python3
import re, cgi, sys, os

import cgitb
cgitb.enable()

extensions = {}
dossiers = {}
numerotation = {'num' :0}

for clef in cgi.FieldStorage().keys():
	dossiers[clef] = cgi.FieldStorage()[clef].value

#-----debut du html et 2 fonction javascript gereaffiche et affichecontenu la derniere utilise jquery------------------ 

print("""Content-type: text/html

<!DOCTYPE html>
<html >
<head>
<meta charset="utf-8" />
<link rel="stylesheet" type="text/css" href="http://localhost/~jchopelet/css/exploreurStyle.css">
<script src='https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js'></script>

<script>
function gereaffiche(id){
var etat = document.getElementById(id).style.display;
if(etat =="none")
	{
	document.getElementById(id).style.display = "block";
	
	}
else
	{
	document.getElementById(id).style.display = "none";
	}
}



function affichecontenu(chemin){
$(document).ready(function(){
$("#contenu").load(chemin);
})
}


</script>
</head>
<body >
<div id='liste'>
<h1>la liste</h1>
<hr class='horiz'>
""")

print("""
<div id= 'div"""+str(numerotation['num'])+"""' style='float: none; display: block'>
<img src='http://localhost/~jchopelet/icondossier/folder.png' width='20' height='20' onclick='gereaffiche(\"div"""+str(numerotation['num']+1)+"""\"); affichecontenu(\"http://localhost/~jchopelet/cgi-bin/contenu4.cgi?repertoire="""+dossiers['repertoire']+"""\")' /> <span>"""+dossiers['repertoire']+"""</span>
</div>
""")

#------definition de la fonction parcoursliste:------------------------------------

def parcoursliste (repertoire):
	print("""
<ul>
<div id= 'div"""+str(numerotation['num']+1)+"""' style='float: none; display: none'>
""")
	liste = os.listdir(repertoire)
	for fichier in liste:
		if os.path.isdir(repertoire + "/" +fichier):
			numerotation['num'] += 1
			print("""
<img src='http://localhost/~jchopelet/icondossier/folder.png' width='20' height='20' onclick='gereaffiche(\"div"""+str(numerotation['num']+1)+"""\"); affichecontenu(\"http://localhost/~jchopelet/cgi-bin/contenu4.cgi?repertoire="""+repertoire+ "/" +fichier+"""\")' /> <span>"""+fichier+"""</span>
""")
			parcoursliste(repertoire+ "/" +fichier)
			
			print("""

</div>
</ul>
""")

#-----appel de la fonction parcoursliste--------------------------------------------

parcoursliste(dossiers['repertoire'])



#-----fin de la balise liste et debut de la balise contenu-----------------------------------------------------------

print("""
</div>
</div>


<div id='contenu'>
<h1>le contenu</h1>
<hr class='horiz'>
</div> 
</body>
</html>
""")
