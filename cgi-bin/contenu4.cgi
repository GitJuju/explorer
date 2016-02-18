#!/usr/bin/env python3

import re, cgi, sys, os
import cgitb
cgitb.enable()

extensions = {}
dossiers = {}

for clef in cgi.FieldStorage().keys():
	dossiers[clef] = cgi.FieldStorage()[clef].value

print("""Content-type: text/html

<html>
<head>
<meta charset="utf-8" />
<link rel = "stylesheet" type = "text/css" href = "contenu.css">
<script src='https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js'></script>

<script>
function affichecontenu(chemin){
$(document).ready(function(){
$("#contenu").load(chemin);
})
}
</script>

</head>
<body>
<h1>le contenu</h1>
<hr class='horiz'>
""")

#------definition de la fonction parcours:----------------------------------

def parcours (repertoire):

	liste = os.listdir(repertoire)
	for fichier in liste:
#-----pour les dossiers------------------------------------------------------
		if os.path.isdir(repertoire + "/" +fichier):
			if re.search("^[^.]",fichier):
				print("""
				<div class = 'fichier' style='float: left'>
				<img src='http://localhost/~jchopelet/icondossier/folder.png' width='50' height='50' onclick ='affichecontenu(\"http://localhost/~jchopelet/cgi-bin/contenu4.cgi?repertoire="""+repertoire+"/"+fichier+"""\")'/> <br/> <span>"""+fichier+"""</span>
				</div>""")

#-----pour les fichiers------------------------------------------------------
		else:
			res1 = re.search("\.(.+$)",fichier)
			if res1:
				ext = res1.group(1)

				fd = open("extensions.txt","r")
				if fd:
					contenu = fd.readlines()
					for ligne in contenu:
						if re.search("/48/"+ext+"\.svg$", ligne):
							extensions[ext] ="+ligne+"
							print("""
					<div class ='fichier' style='float: left'>
					<img src='http://localhost/~jchopelet/iconfichier"""+"/"+ext+""".svg' width='50' height='50' /> <br/> <span>"""+fichier+"""</span>
					</div>""")

			else:
				print("""
			<div class = 'fichier' style='float: left'>
			<img src='http://localhost/~jchopelet/iconfichier/unknown.svg' width='50' height='50' /> <br/> <span>"""+fichier+"""</span>
			</div>""")



#-----appel de la fonction parcours--------------------------------------------

parcours(dossiers['repertoire'])



#-----fin de la page html------------------------------------------------------

print("""
</body>
</html>
""")


