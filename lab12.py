def tri(vazio,h,co):
	for i in range(h):
		vazio[co[0]+i][co[1]] = cara
		for j in range(1,i+1):
			vazio[co[0] + i][co[1]+j] = cara
			vazio[co[0] + i][co[1]-j] = cara
def pombo(subdiv,vazio,h,co):
	if subdiv == 0:
		tri(vazio,h,co)
	else:	
		pombo(subdiv-1,vazio,h//2,co)
		pombo(subdiv-1,vazio,h//2,(co[0]+h//2,co[1]+h//2))
		pombo(subdiv-1,vazio,h//2,(co[0]+h//2,co[1]-h//2))
potencia = int(input())
subdiv = int(input())
cara = input()
h = 2**potencia
l = (h*2)-1
vazio = [[" " for j in range(l)] for i in range(h)]
pombo(subdiv,vazio,h,(0,l//2))
mold = []
alem = []
for i in range(len(vazio[0])+4):
  if i == 0 or i == len(vazio[0])+3:
    mold.append("+")
    alem.append("|")
  else:
    mold.append("-") 
    alem.append(" ") 
moldura = "".join(mold)
alien =  "".join(alem)
print(moldura)
print(alien)
for i in range(h):
  n = "".join(vazio[i])
  print("|",n,"|")
print(alien)
print(moldura) 

