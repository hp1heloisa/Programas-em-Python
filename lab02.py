dist_AB = float(input())
v_A = float(input())
v_B = float(input())
tempoABh = dist_AB/(v_A+v_B)
tempoABmin = tempoABh*60
print(format(tempoABmin,'.2f'),"min")
encontroAB = v_A*tempoABh
print(format(encontroAB, '.2f'),"km")
