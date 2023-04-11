print("Qual ou quais os valores de x, em f(x) = axˆ2 + bx + c?",end= " ")
print("Primeiro determine os valores dos coeficientes:")
y = float(input("f(x) = "))
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
delta = b**2 - 4*a*(c-y)
print(delta)
if(a == 0):
  if(b == 0):
    print("x =",y-c)
  else:  
    x = (y-c)/b
    print("x",x,sep= " = ") 
if(a != 0):
  if(delta < 0):
    print("Não existe raizes reais!")
  elif(delta == 0):
    raiz = -b/(2*a)
    print("Raiz =",raiz)
  else:
    raiz1 = ((-b) + delta**0.5)/(2*a) 
    raiz2 = ((-b) - delta**0.5)/(2*a)  
    print("raiz1 =",format(raiz1, '.2f'))
    print("raiz2 =",format(raiz2,'.2f'))
  

