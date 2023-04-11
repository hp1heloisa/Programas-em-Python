def fibonacci(n):
  if n == 1:
    print(1)
  if n > 1:
    lista = [1,1]
    for i in range(n-2):
      lista.append(lista[i]+lista[i+1])
    for i in range(len(lista)):
      print(lista[i],end=", ")  
  return(lista)    


x = fibonacci(int(input()))


