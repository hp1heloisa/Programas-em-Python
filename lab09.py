def hor(pala): 
  dic[pala] = 0
  for i in range(len(ca)):
    linha = ''.join(ca[i])
    if pala in linha:
      dic[pala] = dic[pala] + 1
      x = linha.index(pala)
      for j in range(len(pala)):
        palavras[i][j+x] = pala[j] 
    ca[i].reverse()
    linha = "".join(ca[i]) 
    if pala in linha:
      dic[pala] = dic[pala] + 1
      y = linha.index(pala)
      palavras[i].reverse()
      for j in range(len(pala)):
        palavras[i][j+y] = pala[j]
      palavras[i].reverse()  
    ca[i].reverse()  
  return dic[pala] 
def vert(pala): 
  dic[pala] = 0
  new = []
  for i in range(len(ca[0])):
    L = []
    for j in range(len(ca)):
      L.append(ca[j][i])
    new.append(L)  
  for i in range(len(new)):
    linha = ''.join(new[i])
    if pala in linha:
      dic[pala] = dic[pala] + 1
      x = linha.index(pala)
      for j in range(len(pala)):
        palavras[x+j][i] = pala[j]
    new[i].reverse()
    linha = "".join(new[i]) 
    if pala in linha:
      dic[pala] = dic[pala] + 1
      y = len(linha) - linha.index(pala) - 1
      w = len(pala) - 1
      for j in range(len(pala)):
        palavras[y-j][i] = pala[j]
    new[i].reverse()  
  return dic[pala]  
def diag(pala): 
  ok = False
  x = 0
  for i in range(len(ca)):
    for j in range(len(ca[0])):
      if ca[i][j] == pala[0]:
        ok = True
        for k in range(len(pala)):
          if (i+k)<len(ca) and (j+k)<len(ca[0]):
            c = i
            d = j
            if ca[i+k][j+k] != pala[k]:
              ok = False
          else:
            ok = False
            break
      if ok:
        break
    if ok:
      break
  if ok:
    x = x + 1
    for i in range(len(pala)):
      palavras[c+i][d+i] = pala[i]
  return x             
def diagcont(pala):
  ok = False
  x = 0
  for i in range(len(ca)):
    ca[i].reverse()
  for i in range(len(ca)):
    for j in range(len(ca[0])):
      if ca[i][j] == pala[0]:
        ok = True 
        c = i 
        d = j 
        for k in range(len(pala)): 
          if (i+k)<len(ca) and (j+k)<len(ca[0]):
            if ca[i+k][j+k] != pala[k]:
              ok = False
          else:
            ok = False
            break
      if ok:
        break
    if ok:
      break
  for i in range(len(ca)):
    ca[i].reverse()    
  if ok:
    x = x + 1
    for i in range(len(palavras)):
      palavras[i].reverse()
    for i in range(len(pala)):
      palavras[c+i][d+i] = pala[i]
    for i in range (len(palavras)):
      palavras[i].reverse()  
  return x            
def diagbaixo(pala):
  ok = False
  x = 0
  ca.reverse()
  for i in range(len(ca)):
    for j in range(len(ca[0])):
      if ca[i][j] == pala[0]:
        ok = True
        for k in range(len(pala)):
          if (i+k)<len(ca) and (j+k)<len(ca[0]):
            c = i 
            d = j
            if ca[i+k][j+k] != pala[k]:
              ok = False
          else:
            ok = False
            break
      if ok:
        break
    if ok:
      break
  ca.reverse()   
  if ok:
    x = x + 1
    palavras.reverse()
    for i in range(len(pala)):
      palavras[c+i][d+i] = pala[i]
    palavras.reverse()  
  return x      
def diagbaixocont(pala):
  ok = False
  x = 0
  ca.reverse()
  for i in range(len(ca)):
    ca[i].reverse()
  for i in range(len(ca)):
    for j in range(len(ca[0])):
      if ca[i][j] == pala[0]:
        ok = True
        for k in range(len(pala)):
          if (i+k)<len(ca) and (j+k)<len(ca[0]):
            c = i 
            d = j
            if ca[i+k][j+k] != pala[k]:
              ok = False
          else:
            ok = False
            break
      if ok:
        break
    if ok:
      break
  for i in range(len(ca)):
    ca[i].reverse()    
  ca.reverse()  
  if ok:
    x = x + 1
    palavras.reverse()
    for i in range(len(palavras)):
      palavras[i].reverse()
    for i in range(len(pala)):
      palavras[c+i][d+i] = pala[i]
    for i in range (len(palavras)):
      palavras[i].reverse()
    palavras.reverse()    
  return x     
txt = input()
ca = []
while not(txt.isdigit()):
  ca.append(txt.split())
  txt = input()
n = int(txt)
c = 0
dic = {}
palavras = [["." for x in range(len(ca[0]))] for y in range(len(ca))]
while c < n: 
  pala = input()
  dic[pala] = vert(pala) + hor(pala) + diag(pala) + diagcont(pala) + diagbaixo(pala) + diagbaixocont(pala)
  c = c + 1  
saida = []
for i in range(len(palavras)):
  x = ""
  for j in range(len(palavras[0])):
      x = x + " " + palavras[i][j]
      x = x.strip()
  saida.append(x)
for i in range(len(saida)):
  print(saida[i])    
lista = sorted(dic)
for i in range(len(lista)):
  print(lista[i],":",sep = "", end = " ")
  print(dic[lista[i]])

