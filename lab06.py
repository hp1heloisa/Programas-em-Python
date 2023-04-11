forma = str(input())
caractere = input()
if forma == "Q":
  lado = int(input())
  if lado < 3:
    print("Dimensao invalida.")
  else:
    print(caractere*lado)
    for i in range(lado-2):
      print(caractere," "*(lado-2),caractere,sep = "")
    print(caractere*lado)
elif forma == "R":
  largura = int(input())
  altura = int(input())  
  if largura < 3 or altura < 3:
    print("Dimensao invalida.")
  else:  
    print(caractere*largura)
    for i in range(altura-2):
      print(caractere," "*(largura-2),caractere,sep = "")
    print(caractere*largura)  
elif forma == "TR":
  altura = int(input())
  if altura < 3:
    print("Dimensao invalida.")
  else:  
    print(caractere)
    c = 0 #espasso entre os caracteres
    for i in range(altura-2):
      print(caractere," "*c,caractere,sep = "")
      c = c + 1
    print(caractere*altura)
elif forma == "TI": #aumenta altura menos 1 na base
  altura = int(input())
  if altura < 3:
    print("Dimensao invalida.")
  else:
    print(" "*(altura-1),caractere,sep = "")
    d = altura-2 #espassamento vazio antes do caractere
    e = 1 #espassamento vazio entre os caracteres
    for i in range(altura-2):
      print(" "*d,caractere," "*e,caractere,sep = "")
      d = d - 1
      e = e + 2
      f = (altura*2)-1 #valor da base  
    print(" "*d,caractere*f,sep = "")  
elif forma == "H":
  lado = int(input())
  if lado < 3:
    print("Dimensao invalida.")
  else:
    print(" "*(lado-2),caractere*lado)
    g = lado-2
    h = lado 
    for i in range(lado-1):
      print(" "*g,caractere," "*h,caractere,sep = "")
      g = g - 1
      h = h + 2
    g = g + 2
    h = h - 4  
    for i in range(lado-2):
      print(" "*g,caractere," "*h,caractere,sep = "") 
      g = g + 1
      h = h - 2
    print(" "*(lado-2),caractere*lado)
elif forma == "QQ":
  lado = int(input())
  largura = int(input())    
  altura = int(input())
  if largura < 1 or altura < 1 or lado < 3:
    print("Dimensao invalida.")
  else: 
    print(caractere*(largura*(lado-1)+1)) 
    for i in range(altura):
      for j in range(lado-2):
        for k in range(largura):
          print(caractere," "*(lado-2),sep = "",end = "") 
        print(caractere)      
      print(caractere*(largura*(lado-1)+1))
elif forma == "X":
  lado = int(input())
  largura = int(input())    
  altura = int(input())
  if largura < 1 or altura < 1 or lado < 3:
    print("Dimensao invalida.")
  else:
    print(caractere*(largura*(lado-1)+1))
    for i in range(1,altura+1):
      if i%2!=0:
        for j in range(lado-2):
          for k in range(1,largura+1):
            if k%2!=0:
              print(caractere," "*(lado-2),sep = "",end = "")
              if k==largura:
                print(caractere)       
            if k%2==0:
              print(caractere*(lado-1),end = "") 
              if k == largura:
                print(caractere)       
      if i%2==0:
        for j in range(lado-2):
          for k in range(1,largura+1):
            if k%2!=0:
              print(caractere*(lado-1),end = "")
              if k == largura:
                print(caractere)
            if k%2==0:
              print(caractere," "*(lado-2),sep = "",end = "") 
              if k == largura:
                print(caractere) 
      print(caractere*(largura*(lado-1)+1))   
else:
  print("Identificador invalido.")         









    
    


