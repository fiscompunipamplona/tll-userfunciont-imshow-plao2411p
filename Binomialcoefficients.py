#2.11 Binomial coefficients

from math import factorial 
def combinatoria(p):
  for i in range(p):
    j=0
    while i>=j:
      c= factorial(i)/(factorial(j)*factorial(i-j))
      j+=1
      print (c,end=" ")
    print("\n")
    
#b
combinatoria(21)

#c  n-> lanzamientos  k-> cara
def probabilidad(n,k):
  p= (factorial(n)/(factorial(k)*factorial(n-k)))/2**n
  return p

  #c-a
print ("Probabilidad de que en 100 lanzamientos caiga cara 60 veces ",probabilidad(100,60))

#c-b
pacum=0
for i in range(60,101):
  pacum+= probabilidad(100,i)
print("Probabilidad de que caiga 60 y mas de 60 veces caras en 100 lanzadas ",pacum)