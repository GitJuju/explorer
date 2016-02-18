function gereaffiche(){

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

gereaffiche();
