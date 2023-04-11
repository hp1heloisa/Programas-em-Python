notasAC = [float(x) for x in input().split()]
mediaAC = sum(notasAC)/len(notasAC)
print("Media das atividades conceituais:",format(mediaAC,".1f"))
def tupla_float_int(x) :
    x = x[1:-1]       
    x = x.split(",")  
    nota = float(x[0])   
    peso = int(x[1])     
    return (nota,peso)      
notaslab = [tupla_float_int(x) for x in input().split()]
soma = 0
divisor = 0
for i in notaslab:
  s = i[0]*i[1]
  soma = soma + s
  divisor = divisor + i[1]
medialabs = soma/divisor
print("Media das tarefas de laboratorio:",format(medialabs,".1f"))
pp1, test, pp2 = map(float,input().split())
mediaprovas = (pp1*2+test*1+pp2*4)/7
print("Media das avaliacoes escritas:",format(mediaprovas,".1f"))
presenca = float(input())
print("Frequencia:",str(presenca)+"%")
if presenca >= 75:
  if mediaprovas >= 5 and medialabs >= 5:
    mediafinal = max(5.0, 0.6 * mediaprovas + 0.3 * medialabs + 0.1 * mediaAC)
    print("Aprovado(a) por nota e frequencia.")
    print("Media final:",format(mediafinal,".1f"))
  elif mediaprovas >= 2.5 and medialabs >= 2.5:
    mediaantes = min(4.9, 0.6 * mediaprovas + 0.3 * medialabs + 0.1 * mediaAC)
    print("Media preliminar:",format(mediaantes,".1f"))
    exame = float(input())
    print("Nota no exame:",exame)
    mediafinal = (mediaantes + exame)/2
    if mediafinal >= 5:
      print("Aprovado(a) por nota e frequencia.")
      print("Media final:",format(mediafinal,".1f"))
    else:
      print("Reprovado(a) por nota.")
      print("Media final:",format(mediafinal,".1f"))
  else:
    mediafinal = min(mediaprovas, medialabs)    
    print("Reprovado(a) por nota.")
    print("Media final:",format(mediafinal,".1f"))
else:
   mediafinal = min(mediaprovas, medialabs)  
   print("Reprovado(a) por frequencia.")
   print("Media final:",format(mediafinal,".1f"))





