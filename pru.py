social = ['amigo','amiga','compañeros','fiesta','amigos']
enc = {'feliz': 'Salir con amigos\nTomar fotos'}
ret=''
antes = ret;
for f in social:
	if(ret==antes):
		if(f in enc['feliz'].lower()):
			ret += "social "

print(ret)
