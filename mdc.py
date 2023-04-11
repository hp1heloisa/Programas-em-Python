m = int(input())
n = int(input())
list = [m,n]
if m == 0 or n == 0:
  print(max(list))
if m!=0 and n!=0:
  div = 2
  contador = 1
  while m > 1 or n > 1:
    if m%div==0 and n%div==0:
      print(m,",",n,"/",div)
      m = m//div
      n = n//div
      contador = contador*div
    elif m%div==0:     
      print(m,",",n,"/",div)  
      m = m//div  
    elif n%div==0:
      print(m,",",n,"/",div)
      n = n//div
    else:  
      div = div + 1 
  print(m,",",n)      
print("MDC =",contador)


