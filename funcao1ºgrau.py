print("Qual o valor de x em uma função da forma",end=" ")
funcao="y = ax + b"
print(funcao,sep= "",end= "? ")
print("Quando:")
y=float(input("y = "))
a=float(input("a = "))
b=float(input("b = "))
print(a,"x",sep= "",end= " + ")
print(b,end=" = ")
print(y)
print(a,"x",sep= "",end= " = ")
print(y-b)
sub=y-b
print("x",sub/a,sep= " = ")
