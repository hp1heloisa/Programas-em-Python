pontuacao = [",",".","...",":","(",")","!","?","-"]
text = str(input(""))
while not("---" in text):
  for i in pontuacao:
    text = text.replace(i," ")
  text = text.lower()
  alem = str(input(""))
  if "---" in alem:
    break
  else:
    text = text + " " + alem  
palavras = text.split()   
dic = {}
print("Vocabulario:")
for j in palavras:
   dic[j] = dic[j] + 1 if j in dic else 1  
for k in sorted(dic):
  print(k," (",dic.get(k),")",sep = "")
print("Sugestoes:")
word = str(input(""))
lista = list(dic.keys())
lista = sorted(lista)
while word != "---":
  suget = ""  
  for l in lista:
    if l.startswith(word) and l!=word:
      suget = suget + " " + l  
  print(word+":", suget,sep = "")
  word = str(input("")).lower()





