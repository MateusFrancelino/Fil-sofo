def validador(usuario,senha):
    for caracter in senha:
      if caracter.isnumeric()==True:
        for caracter in senha:
          if caracter.isalpha()==True:
            for caracter in senha:  
              if caracter.isupper()==True:
                for caracter in senha:
                  if caracter.islower()==True:
                    for caracter in senha:
                      if(('!@#$%¨&*'.find(caracter))>0):
                        return True
    
    return False



usuario = senha =''

teste=False
caracter="a"


while(teste==False):
  usuario=input('informe o nome de usuario: ')
  senha =  (input ('informe sua senha: '))
  if(len(senha)<8):
    valido = False
  else:
    valido = validador(usuario,senha)
  if valido==True:
    teste=True
  else:
    print("Sua senha deve Prencher os seguintes requisitos") 
    print("Ter no minimo 8 caracteres")
    print ("1 letra maiuscula")
    print ("1 letra minuscula")
    print ("1 numero")
    print( "1 caracter especial ! @ # $ % ¨ & * " )
