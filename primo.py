n = int(input())
for i in range (3,n+1):
  maxmenor = []
  while i > 1: 
    div = 2
    contador = 1
    if i%div==0:
      i = i//div
      contador = contador*div
    else:
      div = div + 1
    if contador == i:    
      maxmenor.append(i)    
print(max(maxmenor))
