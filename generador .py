import random

caracter=['+','-','/','*','!','&','$','#','?','=','@','a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
lon=int(input('de cuantos caracteres se compondra la contrasena deseada'))
respuesta=''
for i in range(lon):
    respuesta+=random.choice (caracter)
print(respuesta)
